from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from banco.models.cliente import Cliente


class ClienteTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_criar_cliente(self):
        # dado
        Cliente.objects.create(
            nome="Stephanie Campos Custodio",
            cpf="150.400.800-50",
            dt_nascimento="22.08.1994",
            email="ster@gmail",
            celular="+5521990047270",
            senha="123123"
            )
        # quando
        cliente = Cliente.objects.get(
            nome="Stephanie Campos Custodio"
            )
        # entao
        self.assertEqual(cliente.nome, "Stephanie Campos Custodio") 
