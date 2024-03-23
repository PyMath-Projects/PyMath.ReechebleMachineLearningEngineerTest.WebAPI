import json

from pymongo import MongoClient

from reecheble_finance.application.sdk.dtos.add_loan_account.add_loan_account_response_dto import (
    AddLoanAccountResponseDTO)
from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)


class LoanAccountRepository(AbstractLoanAccountRepository):

    def __init__(self, context: MongoClient) -> None:
        super().__init__(context=context)
        self.database = context['ReechebleFinance']
        self.collection = self.database['ReechebleLoanAccount']

    def list(self):
        pass

    def get(self, **filters):
        pass

    def get_many(self, **filters):
        pass

    def update(self, **kwargs):
        pass

    def delete(self, id_):
        pass

    def sync(self) -> None:
        pass

    def add(self, *, request: LoanAccount) -> AddLoanAccountResponseDTO:
        self.collection.insert_one(json.loads(request.json()))
        return AddLoanAccountResponseDTO(
            id=request.id,
            first_name=request.first_name,
            last_name=request.last_name,
            email_address=request.email_address)
