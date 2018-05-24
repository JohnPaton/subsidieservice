# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account import Account  # noqa: F401,E501
from swagger_server.models.master_account_base import MasterAccountBase  # noqa: F401,E501
from swagger_server.models.transaction import Transaction  # noqa: F401,E501
from swagger_server import util


class MasterAccount(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, description: str=None, iban: str=None, balance: float=None, last_updated: str=None, id: str=None, transactions: List[Transaction]=None):  # noqa: E501
        """MasterAccount - a model defined in Swagger

        :param name: The name of this MasterAccount.  # noqa: E501
        :type name: str
        :param description: The description of this MasterAccount.  # noqa: E501
        :type description: str
        :param iban: The iban of this MasterAccount.  # noqa: E501
        :type iban: str
        :param balance: The balance of this MasterAccount.  # noqa: E501
        :type balance: float
        :param last_updated: The last_updated of this MasterAccount.  # noqa: E501
        :type last_updated: str
        :param id: The id of this MasterAccount.  # noqa: E501
        :type id: str
        :param transactions: The transactions of this MasterAccount.  # noqa: E501
        :type transactions: List[Transaction]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'iban': str,
            'balance': float,
            'last_updated': str,
            'id': str,
            'transactions': List[Transaction]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'iban': 'iban',
            'balance': 'balance',
            'last_updated': 'last_updated',
            'id': 'id',
            'transactions': 'transactions'
        }

        self._name = name
        self._description = description
        self._iban = iban
        self._balance = balance
        self._last_updated = last_updated
        self._id = id
        self._transactions = transactions

    @classmethod
    def from_dict(cls, dikt) -> 'MasterAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The master-account of this MasterAccount.  # noqa: E501
        :rtype: MasterAccount
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this MasterAccount.


        :return: The name of this MasterAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this MasterAccount.


        :param name: The name of this MasterAccount.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this MasterAccount.


        :return: The description of this MasterAccount.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this MasterAccount.


        :param description: The description of this MasterAccount.
        :type description: str
        """

        self._description = description

    @property
    def iban(self) -> str:
        """Gets the iban of this MasterAccount.


        :return: The iban of this MasterAccount.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban: str):
        """Sets the iban of this MasterAccount.


        :param iban: The iban of this MasterAccount.
        :type iban: str
        """

        self._iban = iban

    @property
    def balance(self) -> float:
        """Gets the balance of this MasterAccount.


        :return: The balance of this MasterAccount.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        """Sets the balance of this MasterAccount.


        :param balance: The balance of this MasterAccount.
        :type balance: float
        """

        self._balance = balance

    @property
    def last_updated(self) -> str:
        """Gets the last_updated of this MasterAccount.


        :return: The last_updated of this MasterAccount.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: str):
        """Sets the last_updated of this MasterAccount.


        :param last_updated: The last_updated of this MasterAccount.
        :type last_updated: str
        """

        self._last_updated = last_updated

    @property
    def id(self) -> str:
        """Gets the id of this MasterAccount.


        :return: The id of this MasterAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this MasterAccount.


        :param id: The id of this MasterAccount.
        :type id: str
        """

        self._id = id

    @property
    def transactions(self) -> List[Transaction]:
        """Gets the transactions of this MasterAccount.


        :return: The transactions of this MasterAccount.
        :rtype: List[Transaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions: List[Transaction]):
        """Sets the transactions of this MasterAccount.


        :param transactions: The transactions of this MasterAccount.
        :type transactions: List[Transaction]
        """

        self._transactions = transactions
