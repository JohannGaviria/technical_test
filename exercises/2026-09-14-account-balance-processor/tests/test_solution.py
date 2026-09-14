import pytest
from solution.solution import process_operations


class TestDeposits:
    def test_single_deposit(self):
        result = process_operations(0, [{"type": "deposit", "amount": 100}])
        assert result["balance"] == 100
        assert result["operations"]["deposit"] == 1
        assert result["operations"]["withdraw"] == 0
        assert result["operations"]["transfer"] == 0

    def test_multiple_deposits(self):
        ops = [
            {"type": "deposit", "amount": 500},
            {"type": "deposit", "amount": 300},
        ]
        result = process_operations(200, ops)
        assert result["balance"] == 1000
        assert result["operations"]["deposit"] == 2

    def test_deposit_updates_max_balance(self):
        ops = [
            {"type": "deposit", "amount": 500},
            {"type": "withdraw", "amount": 200},
        ]
        result = process_operations(1000, ops)
        assert result["max_balance"] == 1500


class TestWithdrawals:
    def test_successful_withdrawal(self):
        result = process_operations(500, [{"type": "withdraw", "amount": 200}])
        assert result["balance"] == 300
        assert result["operations"]["withdraw"] == 1

    def test_failed_withdrawal_insufficient_funds(self):
        result = process_operations(100, [{"type": "withdraw", "amount": 500}])
        assert result["balance"] == 100
        assert result["operations"]["withdraw"] == 0

    def test_withdrawal_to_zero(self):
        result = process_operations(500, [{"type": "withdraw", "amount": 500}])
        assert result["balance"] == 0
        assert result["operations"]["withdraw"] == 1


class TestTransfers:
    def test_transfer_no_fee(self):
        result = process_operations(1000, [{"type": "transfer", "amount": 500, "to": "alice"}])
        assert result["balance"] == 500
        assert result["fees"] == 0
        assert result["operations"]["transfer"] == 1

    def test_transfer_with_fee(self):
        result = process_operations(5000, [{"type": "transfer", "amount": 2000, "to": "bob"}])
        assert result["balance"] == 2970
        assert result["fees"] == 30.0
        assert result["operations"]["transfer"] == 1

    def test_failed_transfer_insufficient_funds(self):
        result = process_operations(100, [{"type": "transfer", "amount": 200, "to": "charlie"}])
        assert result["balance"] == 100
        assert result["fees"] == 0
        assert result["operations"]["transfer"] == 0


class TestMixedOperations:
    def test_example_1(self):
        ops = [
            {"type": "deposit", "amount": 500},
            {"type": "withdraw", "amount": 200},
            {"type": "transfer", "amount": 300, "to": "alice"},
        ]
        result = process_operations(1000, ops)
        assert result["balance"] == 1000
        assert result["max_balance"] == 1500
        assert result["fees"] == 0
        assert result["operations"] == {"deposit": 1, "withdraw": 1, "transfer": 1}

    def test_example_2(self):
        ops = [{"type": "transfer", "amount": 2000, "to": "bob"}]
        result = process_operations(5000, ops)
        assert result["balance"] == 2970
        assert result["fees"] == 30.0

    def test_example_3(self):
        ops = [{"type": "withdraw", "amount": 500}]
        result = process_operations(100, ops)
        assert result["balance"] == 100
        assert result["operations"]["withdraw"] == 0


class TestEmptyOperations:
    def test_no_operations(self):
        result = process_operations(500, [])
        assert result["balance"] == 500
        assert result["max_balance"] == 500
        assert result["fees"] == 0
        assert result["operations"] == {"deposit": 0, "withdraw": 0, "transfer": 0}

    def test_initial_balance_zero_no_operations(self):
        result = process_operations(0, [])
        assert result["balance"] == 0
        assert result["max_balance"] == 0
