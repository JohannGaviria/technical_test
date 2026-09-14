import pytest
from solution.solution import process_operations


class TestBoundaryConditions:
    def test_transfer_exactly_at_fee_threshold(self):
        result = process_operations(5000, [{"type": "transfer", "amount": 1000, "to": "alice"}])
        assert result["balance"] == 4000
        assert result["fees"] == 0

    def test_transfer_just_above_fee_threshold(self):
        result = process_operations(5000, [{"type": "transfer", "amount": 1000.01, "to": "alice"}])
        expected_fee = round(1000.01 * 0.015, 2)
        assert result["balance"] == pytest.approx(5000 - 1000.01 - expected_fee)
        assert result["fees"] == pytest.approx(expected_fee)

    def test_withdraw_exact_balance(self):
        result = process_operations(250.75, [{"type": "withdraw", "amount": 250.75}])
        assert result["balance"] == 0
        assert result["operations"]["withdraw"] == 1

    def test_withdraw_one_cent_over_balance(self):
        result = process_operations(100, [{"type": "withdraw", "amount": 100.01}])
        assert result["balance"] == 100
        assert result["operations"]["withdraw"] == 0


class TestFailedTransfersNoFee:
    def test_failed_transfer_no_fee_charged(self):
        ops = [
            {"type": "transfer", "amount": 500, "to": "alice"},
            {"type": "transfer", "amount": 600, "to": "bob"},
        ]
        result = process_operations(500, ops)
        assert result["balance"] == 0
        assert result["fees"] == 0
        assert result["operations"]["transfer"] == 1

    def test_failed_transfer_with_fee_threshold_no_fee(self):
        ops = [{"type": "transfer", "amount": 2000, "to": "alice"}]
        result = process_operations(500, ops)
        assert result["balance"] == 500
        assert result["fees"] == 0
        assert result["operations"]["transfer"] == 0

    def test_multiple_failed_transfers_no_fees(self):
        ops = [
            {"type": "transfer", "amount": 1500, "to": "alice"},
            {"type": "transfer", "amount": 1500, "to": "bob"},
            {"type": "transfer", "amount": 1500, "to": "charlie"},
        ]
        result = process_operations(100, ops)
        assert result["balance"] == 100
        assert result["fees"] == 0
        assert result["operations"]["transfer"] == 0


class TestMaxBalanceTracking:
    def test_max_balance_at_initial(self):
        ops = [
            {"type": "withdraw", "amount": 100},
            {"type": "withdraw", "amount": 100},
        ]
        result = process_operations(1000, ops)
        assert result["max_balance"] == 1000

    def test_max_balance_mid_sequence(self):
        ops = [
            {"type": "deposit", "amount": 500},
            {"type": "withdraw", "amount": 300},
            {"type": "deposit", "amount": 100},
        ]
        result = process_operations(1000, ops)
        assert result["max_balance"] == 1500

    def test_max_balance_after_failed_operations(self):
        ops = [
            {"type": "deposit", "amount": 500},
            {"type": "withdraw", "amount": 1000},
            {"type": "withdraw", "amount": 1000},
        ]
        result = process_operations(1000, ops)
        assert result["max_balance"] == 1500
        assert result["balance"] == 1500

    def test_max_balance_with_transfer(self):
        ops = [
            {"type": "deposit", "amount": 1000},
            {"type": "transfer", "amount": 1500, "to": "alice"},
        ]
        result = process_operations(1000, ops)
        expected_fee = round(1500 * 0.015, 2)
        assert result["max_balance"] == 2000
        assert result["balance"] == pytest.approx(2000 - 1500 - expected_fee)


class TestFeeCalculations:
    def test_multiple_transfers_with_fees(self):
        ops = [
            {"type": "transfer", "amount": 2000, "to": "alice"},
            {"type": "transfer", "amount": 3000, "to": "bob"},
        ]
        result = process_operations(10000, ops)
        fee1 = round(2000 * 0.015, 2)
        fee2 = round(3000 * 0.015, 2)
        assert result["fees"] == pytest.approx(fee1 + fee2)
        assert result["balance"] == pytest.approx(10000 - 2000 - fee1 - 3000 - fee2)

    def test_fee_rounding(self):
        ops = [{"type": "transfer", "amount": 1001, "to": "alice"}]
        result = process_operations(5000, ops)
        expected_fee = round(1001 * 0.015, 2)
        assert result["fees"] == expected_fee


class TestConsecutiveFailures:
    def test_all_operations_fail(self):
        ops = [
            {"type": "withdraw", "amount": 1000},
            {"type": "withdraw", "amount": 500},
            {"type": "transfer", "amount": 200, "to": "alice"},
        ]
        result = process_operations(100, ops)
        assert result["balance"] == 100
        assert result["operations"] == {"deposit": 0, "withdraw": 0, "transfer": 0}
        assert result["fees"] == 0
        assert result["max_balance"] == 100

    def test_mix_of_success_and_failure(self):
        ops = [
            {"type": "withdraw", "amount": 1000},
            {"type": "deposit", "amount": 500},
            {"type": "withdraw", "amount": 300},
            {"type": "transfer", "amount": 500, "to": "alice"},
        ]
        result = process_operations(100, ops)
        assert result["balance"] == 800
        assert result["operations"]["deposit"] == 1
        assert result["operations"]["withdraw"] == 1
        assert result["operations"]["transfer"] == 1
        assert result["max_balance"] == 600


class TestLargeAmounts:
    def test_large_deposit(self):
        result = process_operations(0, [{"type": "deposit", "amount": 100000}])
        assert result["balance"] == 100000
        assert result["max_balance"] == 100000

    def test_large_transfer_with_fee(self):
        result = process_operations(100000, [{"type": "transfer", "amount": 50000, "to": "alice"}])
        expected_fee = round(50000 * 0.015, 2)
        assert result["balance"] == pytest.approx(100000 - 50000 - expected_fee)
        assert result["fees"] == pytest.approx(expected_fee)
