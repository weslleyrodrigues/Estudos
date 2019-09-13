#De dentro do arquivo veículo, importe a classe Veículo
from veiculo import Veiculo

caminhao = Veiculo('rosa',6,'ford',50)

print(caminhao)
print(type(caminhao),'\n')

print('Este caminhao é da cor: *',caminhao.cor,'* da marca: ',caminhao.marca,' e tem ',caminhao.rodas,' rodas','. Seu tanque é de: ',caminhao.tanque,' litros')

carro = Veiculo('azul',4,'fiat',30)
print('Este Carro é da cor: *', carro.cor,'* da marca: ',carro.marca,' tem ',carro.rodas,' rodas','. Seu tanque é de: ',carro.tanque,' litros')
carro.abastecer(10)
print('litros no tanque: ',carro.tanque)