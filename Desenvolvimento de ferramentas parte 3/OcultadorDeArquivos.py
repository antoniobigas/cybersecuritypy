import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFilterAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")


