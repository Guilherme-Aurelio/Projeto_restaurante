## INTRODUÇÃO

<div style="text-align: justify">
O projeto descrito neste relatório foi elaborado pelos seguintes alunos do segundo período do curso de Tecnologia em Sistemas para Internet do Instituto Federal do Rio Grande do Norte do campus de Parnamirim: Andriéria Azevedo Dantas, Emilly Jennifer Martins dos Santos, Guilherme Aurelio Ribeiro Rocha, Kelvin Cristiano Marques de Lima e Sarah Letícia da Silva Freire. O trabalho em questão tem como principal objetivo o desenvolvimento de um sistema de controle de pedidos de um restaurante utilizando os softwares: QtCreator, Qt Designer, Microsoft Visual Studio Code e MySQL.
</div>

## EXPLICAÇÃO DO LAYOUT

<div style="text-align: justify">
Em princípio, foi pensado no primeiro layout contendo três tabelas destinadas ao cadastro, a edição e a exclusão dos pratos selecionados pelo restaurante. Na primeira tabela, foram implementados nome, descrição, valor e um campo em branco para a inserção de cada informação. Na segunda tabela, os mesmos itens da parte de cadastro foram colocadas, além de uma caixa de seleção (QComboBox) para escolher qual produto será editado. Já para a terceira tabela, foi colocado também apenas uma caixa de seleção para selecionar qual produto será excluído, apagando as informações sobre nome, descrição e valor. 
</div>

<p align="center">
  <img src="Print_1.png" />
</p>

_Layout 1_ (Figura 1)

<div style="text-align: justify">
O segundo layout apresenta uma parte destinada à exibição do pedido do cliente. Em relação a parte do cardápio, uma caixa de seleção irá conter o nome do produto junto com o seu valor; (o nome do negócio da caixa com seta) mostrará a quantidade daquele determinado produto; e abaixo deles dois haverá uma (caixa) exibindo a descrição do prato selecionado. Abaixo dessa parte, o layout mostra uma parte semelhante a um carrinho de compras, em que mostrará de forma ordenada, os produtos selecionados pelo cliente, seus respectivos valores e quantidades. Além disso, mostrará a quantidade e o preço total do pedido realizado.  
</div>

<p align="center">
  <img src="Print_2.png" />
</p>

_Layout 2_ (Figura 2)


## DIAGRAMA UML

<p align="center">
  <img src="Print_3.png" />
</p>
<p align="center">
  <img src="Print_4.png" />
</p>

UML (Figura 3)

## LÓGICA DO PROJETO

    Método showCBoxs( ):

<div style="text-align: justify">
Em relação a parte lógica do trabalho, primeiramente foi pensado no método showCBoxs( ) para que o nome do produto inserido no cadastro aparecesse no comboBox das partes da edição, da exclusão e do cardápio.
</div>

<p align="center">
  <img src="Print_5.png" />
</p>

_Método showCBoxs( )_ (Figura 4)

<div style="text-align: justify">
Assim, na linha 475 do código, foi definido que o valor da variável (nome_cad) cadastrada se transformasse em string pelo método do QLineEdit chamado text( ). Além disso, como mostrado nas linhas 477 a 480, a estrutura de condição “if” define que se a QLineEdit “nome_cad” não estiver vazia, deve ser repetido a estrutura de repetição “for” contida na variável items. Ou seja, permite que seja cadastrado mais de um produto e todos eles apareçam nos comboBox da edição (linha 478), da exclusão (linha 478) e do cadastro (linha 480). Dentro desse “if”, contém uma outra estrutura condicional “if” (linha 482) que define que se o produto não estiver na lista contida no comboBox da edição, exclusão e do cardápio, então o produto em questão deve ser adicionado neles, através do addItem( ), método responsável por adicionar itens a caixa de seleção(comboBox).
</div>

<p align="center">
  <img src="Print_6.png" />
</p>

_Produto “Sorvete” sendo cadastrado e ainda não aparecendo no comboBox_ (Figura 5)

<p align="center">
  <img src="Print_7.png" />
</p>

_Produto “Sorvete” já foi cadastrado e aparece no comboBox_ (Figura 6)

    Método addCBoxs( ):
<div style="text-align: justify">
Outro método é o AddCBoxs, que junto ao método showCBox é responsável por mostrar os produtos nos comboBoxs na parte de edição, exclusão e cardápio. Nas linhas 506 a 508, é observado que as variáveis “desc”, “nome” e “valor” foram declaradas e representam, respectivamente, a descrição, o nome e o valor monetário do produto em questão. Desse modo, a função text( ) definida nessas linhas, faz com que os valores colocados nessas variáveis sejam string. 
</div>

<p align="center">
  <img src="Print_8.png" />
</p>

_Declaração de variáveis e criação de dicionários no método addCBoxs( )_ (Figura 7)

<div style="text-align: justify">
Além disso, nas linhas 513 e 514, foram criados dois dicionários para a “desc” e “valor” com a chave de identificação sendo o nome do produto. Portanto, podemos estabelecer uma relação entre o produto selecionado, seu valor e sua descrição, fazendo com que, quando o restaurante edita o produto bolo alterando seu valor, por exemplo, o método AddCBoxs permite que a edição ocorra no valor daquele bolo em questão ao invés de ser criado um novo produto, evitando assim uma repetição desnecessária. 
</div>

<p align="center">
  <img src="Print_9.png" />
</p>

_Continuação do método addCBoxs( )_ (Figura 8)

<div style="text-align: justify">
Ademais, nas linhas 518 e 519, indicam que a descrição (desc_dict) e o valor (valor_dict) do produto indicado apareçam nas suas respectivas QLines. Nas últimas linhas (521 a 523) deste método, pela função clear( ), é definido que os valores das variáveis “desc_cad”, “nome_cad” e “valor_cad” fiquem vazias novamente após um cadastro efetivado.
</div>

    Método removeProduto( ): 

<div style="text-align: justify">
OBS: Quando é cadastrado o primeiro produto na parte do cadastro, este recebe um índice ao ir para os QcomboBox de edição, exclusão e cardápio. Como por exemplo na figura 9, o índice do bolo seria 1, o da macarronada seria 2 e assim por diante. Dessa maneira, percebemos que o índice 0 seria o da comboBox vazia.
</div>


<p align="center">
  <img src="Print_10.png" />
</p>

_Produtos do restaurante presentes no comboBox ds parte de edição_ (Figura 9)

<div style="text-align: justify">
Tendo isso em vista, pontua-se que a variável “current_index_cb_edi”, presente na figura 9, refere-se à posição atual de um determinado produto dentro da comboBox. Assim, para a parte de exclusão, foi utilizado o método removeProduto( ) que determina que o prato selecionado no QcomboBox seja excluído a partir do seu índice, sendo removido da “lista” dos QcomboBox da parte de exclusão, edição e cardápio como observado nos exemplos abaixo.
</div>

<p align="center">
  <img src="Print_11.png" />
</p>

_Código do método removeProduto( )_ (Figura 10)

<div style="text-align: justify">
OBS: O atributo comboBox_exc.setCurrentIndex(0) faz com que o QcomboBox volte ao índice 0 para aparecer vazio na exclusão.</div>

<p align="center">
  <img src="Print_12.png" />
</p>

_Lista de produtos da comboBox da exclusão_ (Figura 11)

<p align="center">
  <img src="Print_13.png" />
</p>
 
_Produto "Tapioca" selecionado para a exclusão_ (Figura 12)

<p align="center">
  <img src="Print_14.png" />
</p>

_Produto "Tapioca" foi removido da comboBox_ (Figura 13)

    Método updateLabelDescricao( ):

<div style="text-align: justify">
Na parte do cardápio, percebemos que quando selecionamos um produto presente no comboBox, automaticamente aparecem nas QLabel o seu respectivo valor e descrição. Para que isso aconteça, foi criado o método updateLabelDescricao( ). Nele, observamos a presença do currentText( ) na linha 482 do código, referenciando o produto selecionado da comboBox do cardápio. Nas linhas 483 e 484 foram definidos dicionários para as descrições (variável "desc") e para os valores (variável "valor") possuindo como chave o nome do produto. Dessa maneira, é possível "chamar" para as QLabel, a descrição e o valor do produto desejado, visto que pelo dicionário foi estabelecida uma relação entre eles. Por fim, nas linhas 485 e 486, observa-se a presença do método setText( ) nas variáveis “label_desc_card” e “label_valor_card” que vai ser responsável por alterar o texto dessas variáveis.
</div>

<p align="center">
  <img src="Print_15.png" />
</p>

_código do método UpdateLabelDescricao( )_ (Figura 14)

    Método showNotaFiscal( ):

<div style="text-align: justify">
Outro método criado foi o showNotaFiscal( ) para mostrar os produtos desejados e suas informações, semelhante justamente a uma nota fiscal. Com isso, na linha 558 da figura 15, foi criada uma lista chamada “exibir” para mostrar nessa nota o nome, valor e descrição do produto, bem como sua quantidade e o valor total da compra. Além disso, na linha 561 bem como nas linhas 563 e 564, percebemos o currentText( ) e os dicionários da descrição e do valor do produto vistos anteriormente neste relatório, com o objetivo de haver uma ligação entre o determinado produto desejado, sua respectiva descrição e seu respectivo valor, para assim, quando o produto for escolhido, apareça a descrição e o valor. Na linha 563, também é observado que a variável “quant” foi declarada (quantidade do produto) para que esse tal dado aparecesse na parte do cardápio e também na QLabel da nota fiscal. Com a presença do método value( ) nessa linha, qualquer coisa digitada na sua spinBox seria considerado um valor. 
</div>

<p align="center">
  <img src="Print_16.png" />
</p>

_ Início do método showNotaFiscal( )_ (Figura 15)

<div style="text-align: justify">
Na nota fiscal, foi pensado que além de aparecer o nome, descrição, valor e a quantidade unitária de item, também aparecesse o valor total da compra feita pelo cliente. Dessa maneira, na linha 570 da figura 16, foi criada uma estrutura condicional em que define que, primeiramente, o valor unitário (variável "valor") do produto se transforme de string para float para que ocorra a multiplicação dele com a quantidade do item (variável "quant"), como pode ser visto nas linhas 571 e 572 em que a variável "multiplicacao" guarda esse cálculo. Então, para se ter o valor total da compra, a variável "total" irá guardar os valores da variável "multiplicacao" como visto na linha 573 da figura 16, entretanto, percebe-se que o "self.total" não foi declarado dentro do metodo showNotaFiscal( ). Isso foi feito para que não aconteça uma sobreposição dos objetos e dos seus valores quando ocorrer a soma dos valores unitários. Por exemplo: produto A custa 10 reais e produto B custa 10 reais, assim, quando o produto B aparecer na nota fiscal, o valor total (variável “total”) não será 10 e sim 20 reais. Por fim, a variável valor é transformada novamente de float para string para ser exibida na QLabel da nota fiscal. Na linha 578, define que se não ocorrer o “if”, então irá exibir a mensagem de “Valor inválido!”.
</div>

<p align="center">
  <img src="Print_17.png" />
</p>

_continuação do método showNotaFiscal( )_ (Figura 16)

<div style="text-align: justify">
OBS: Observando a figura 17, percebemos também que a lista “exibir_todos_ped” está fora do método para que não se repetida várias vezes a cada objeto que é adicionado a nota fiscal.
</div>

<p align="center">
  <img src="Print_18.png" />
</p>

_Declaração das listas lista_total e exibir_todos_ped fora do método showNotaFiscal( )_ (Figura 17)

<div style="text-align: justify">
Nas linhas da 583 a 594 da figura 18, é mostrado que variável “quant” (quantidade do produto) e a variável “multiplicacao” se transformaram em string(a quantidade sendo agora “quant_string”) e as variáveis quant_string, valor, nome e descricao e multiplicacao sofrem append, ou seja, são adicionadas na lista chamada exibir mostrada no início do método showNotaFiscal( ). Na linha 596 é solicitado por meio de um print que a lista “exibir” seja exibida.
</div>

<p align="center">
  <img src="Print_19.png" />
</p> 
_Continuação do método showNotaFiscal( ):_ (Figura 18)

<div style="text-align: justify">
Como apresentado na linha 434 da figura 17, é observado que foi instanciado a lista “exibir_todos_ped” e na linha 435 da mesma figura, é notado que a string sofre append e é adicionada dentro dessa lista. Dessa maneira, na linha 598 da figura 19, é declarada na variável “lista”, em que com o método join( ), os itens da lista “exibir” sejam separados por um separador. Assim, as linhas 600 a 602 da figura 19, mostram que a string da variável “lista” seja colocada na lista “exibir_todos_ped”, separando cada item (como QUANT ou V UNIT presentes na figura 17) com o separador “ - “ e que a cada um transferido para a nota fiscal, seja colocado abaixo um do  outro como mostrado na figura 20.
</div>

<p align="center">
  <img src="Print_20.png" />
</p>

_Método join( ) presente no showNotaFiscal_ (Figura 19)


<p align="center">
  <img src="Print_21.png" />
</p>

_Exemplo de nota fiscal_ (Figura 20)

<div style="text-align: justify">
Ainda na figura 19, percebemos que o separador da lista exibir_todos_ped muda para “  “ e o preço total (total) é transformado em string para aparecer no final da nota fiscal. Quando a ação de finalizar o pedido é realizada, o comboBox volta para seu índice 0 e o spinBox volta a ter o valor 0.
</div>

    Método editCBoxs( ):

<div style="text-align: justify">
Outro método criado foi o editCBoxs( ) que é responsável pela edição dos comboBoxs quando um produto é editado ou excluído. Desse modo, na linha 614 da figura 21, é definido uma variável chamada “indice” que é o valor da posição de um produto na comboBox, em específico desta linha, na comboBox da parte de edição. Com isso, da linha 617 a 619, as variáveis “desc”, “nome” e “valor” têm seus valores definidos e são transformadas em string pelo método text( ) e das linhas 621 a 623, o produto selecionado de acordo com o seu índice e seu nome irá ser alterado nos comboBoxs da parte de edição, exclusão e cardápio.
</div>

<p align="center">
  <img src="Print_22.png" />
</p>

_Método editCBoxs( )_ (Figura 21)

<div style="text-align: justify">
Após isso, nas linhas 628 e 629, são definidos dois dicionários para as variáveis “desc” e “valor”. Nas linhas 631 a 633, é apresentado atributos que, por meio da função clear( ), irá apagar os valores nome, desc (descrição) e valor (valor unitário do produto). Por fim, na linha 588, mostra a função setCurrentIndex(0) que faz com que o QcomboBox da parte de edição volte ao índice 0.
</div>

<p align="center">
  <img src="Print_23.png" />
</p>
_Continuação do Método editCBoxs_(Figura 22)

    Métodos showMessage( ):

<div style="text-align: justify">
Além disso, quando um produto é cadastrado, editado ou mesmo excluído, aparece uma janela relatando que aquela determinada ação foi realizada. Portanto, os métodos showMessageCad( ), showMessageExc( ) e showMessageEdi( ) definem a variável message_box (a mensagem que vai aparecer no box) que recebe o QMessageBox( ), widget utilizado para exibir caixas de mensagem. Assim, ao final do método, é observado que o widget (QMessageBox( )) é executado aparecendo uma determinada string, como no caso do showMessageCad( ) que aparece "Cadastro realizado."
</div>  

<p align="center">
  <img src="Print_24.png" />
</p>

_Método showMessage() sendo aplicadop para cadastro, edição e exclusão respectivamente_ (Figura 23)

<p align="center">
  <img src="Print_25.png" />
</p>

(Figura 24)

<p align="center">
  <img src="Print_26.png" />
</p>

(Figura 25)

<p align="center">
  <img src="Print_27.png" />
</p>

(Figura 26)

    Método cancBotCad( ):

<div style="text-align: justify">
Na figura 27 é mostrado o método canBotCad( ), responsável por cancelar o cadastro quando o botão “cancelar” é clicado e que define o método clear( ) para as variáveis desc_cad (descrição na parte de cadastro), nome_cad (nome do produto na parte de cadastro) e valor (valor unitário do produto na parte de cadastro). Com este método, ocorrerá a remoção dos valores das variáveis declaradas no método, sendo excluídos os valores na parte de cadastro. 
</div>  


<p align="center">
  <img src="Print_28.png" />
</p>

_Método cancBotCad( )_ (Figura 27)

    Método cancBotEdi( ):

<div style="text-align: justify">
Na figura 28, o método cancBotEdi( ) é apresentado, sendo responsável pelo cancelamento de uma edição ao clicar no botão de cancelar. Além disso, este método possui as mesmas funções do método cancBotCad( ), diferenciado-se no nome das variáveis (neste método, a descrição do produto é chamada desc_edi, visto que a descrição em questão é da parte de edição e não de cadastro) e na presença do atributo "self.comboBox_edi.setCurrentIndex(0)" que faz com que as QLines das variáveis desc_edi, nome_edi e valor_edi depois de ocorrer a edição de um proibido, voltem à posição zero, ou seja, que elas voltem a serem vazias. 
</div>  

<p align="center">
  <img src="Print_29.png" />
</p>

_Método canBotEdi( )_ (Figura 28)

    Método cancPedido( ):

<div style="text-align: justify">
O método cancPedido( ) é declarado nas linhas da figura 29, e é responsável por cancelar o pedido ao clicar o botão cancelar da parte da nota fiscal. Além disso, são declarados os atributos label nota (referente ao espaço que a nota fiscal será exibida) e label_Vtotal com ambos contendo o método clear( ), para assim limpar os campos do valor total e da nota fiscal. A lista exibir_todos_ped está presente no método, pois quando os dois atributos citados anteriormente são excluídos, a lista precisa está presente para que apareça novamente a string mostrada na linha 664 que aparece apenas uma vez na nota fiscal.
</div> 

<p align="center">
  <img src="Print_30.png" />
</p>

_Método cancPedido( )_ (Figura 29)

    Método canBotExc( ):

<div style="text-align: justify">
Outro método definido nas linhas 666 e 667 da figura abaixo é o cancBotExc( ). Ele é responsável pela exclusão de um produto do sistema. Tal produto acaba saindo dos comboBoxs da parte da edição, exclusão e do cardápio. Assim, o atributo "self.comboBox_exc.setCurrentIndex(0)" acaba fazendo com que o comboBox da parte de exclusão volte a posição 0, depois da exclusão de um determinado produto. 
</div>

<p align="center">
  <img src="Print_31.png" />
</p>

_Método cancBotExc( )_ (Figura 30)

    Método showMessage( ):

<div style="text-align: justify">
Quando o cliente quer finalizar seu pedido, aparece uma janela relatando que aquela ação foi realizada. Portanto, o método showMessageFinPed( ), semelhante aos outros métodos showMessage( ), define também a variável message_box que recebe o QMessageBox( )  (widget que exibe caixas de mensagem). Desse modo, é observado que o widget é executado aparecendo a string determinada no código, além de que, como definidos nas linhas 673 a 677, após a finalização do pedido e do aparecimento da caixa de mensagem, os campos da parte da nota fiscal, label_nota e label_VTotal, ficam vazios.
</div>

<p align="center">
  <img src="Print_32.png" />
</p>

_Método para finalizar o pedido do cliente_ (Figura 31)

<p align="center">
  <img src="Print_33.png" />
</p>

(Figura 32)

    Criação de atributos fora dos métodos:

<div style="text-align: justify">
Observando as linhas 417 a 419 da figura 33, percebemos a declaração dos dicionários referentes à descrição, valor unitário do produto e a quantidade dele que são utilizados diversas vezes por diferentes métodos durante o código do projeto. Além disso, na mesma figura, vemos que são declarados atributos com o método addItem( ) com o objetivo de adicionar os produtos (itens) aos comboBox presentes na parte da edição, exclusão e do cardápio. 
</div>

<p align="center">
  <img src="Print_34.png" />
</p>

_ Declarações de atributos fora dos seus métodos._ (Figura 33)

    Botões de “OK” e “Cancelar”: 

<div style="text-align: justify">
Para que os métodos showCBox( ) e addCBoxs( ) funcionem corretamente, é necessário a criação dos atributos das linhas 416 e 425 da figura 34, que estão ligados com o botão “OK” da figura 35.
</div>

<p align="center">
  <img src="Print_35.png" />
</p>

(Figura 34)

<p align="center">
  <img src="Print_36.png" />
</p>

_Botão “OK” para concluir o cadastro do produto_ (Figura 35)

<div style="text-align: justify">
Para que os métodos showMessageCad( ), showMessageExc( ) e showMessageEdi( ) presentes nas linhas 421 a 423 da figura 36 funcionem corretamente, é necessário a criação desses atributos presentes na imagem, que estão ligados com o botão “OK” das figuras 24, 25 e 26 presentes no relatório
</div>


<p align="center">
  <img src="Print_37.png" />
</p>

(Figura 36)

<div style="text-align: justify">
Por fim, para que os métodos showNotaFiscal( ) e editBox( ) presentes nas linhas 424 e 425 da figura acima funcionem corretamente, é necessário a criação desses atributos presentes na imagem, que estão ligados com o botão “OK” das figuras 37 e 38
</div>


<p align="center">
  <img src="Print_38.png" />
</p>

_Botão para confirmar a edição e o método editBox( )_ (Figura 37)


<p align="center">
  <img src="Print_39.png" />
</p>

_Botão “OK” para confirmar escolha do item e para que este produto apareça na nota fiscal_ (Figura 38)

<div style="text-align: justify">
Para que os métodos cancBotCad( ), cancBotEdi( ), cancPedido( ) e cancBotExc( ) presentes nas linhas 426 a 426 da figura 39 funcionem corretamente, é necessário a criação desses atributos presentes na imagem, que estão ligados com o botão “CANCELAR” das figuras 40, 41, 42 e 43 respectivamente.
</div>

<p align="center">
  <img src="Print_40.png" />
</p>

_Botão “CANCELAR” para cancelar o cadastro_ (Figura 39)

<p align="center">
  <img src="Print_41.png" />
</p>

_Botão “CANCELAR” para cancelar a edição de um produto_ (Figura 40)

<p align="center">
  <img src="Print_43.png" />
</p>

_Botão “CANCELAR” para cancelar o pedido_ (Figura 41)

<p align="center">
  <img src="Print_44.png" />
</p>

_Botão “CANCELAR” para cancelar a edição de um produto_ (Figura 42)

<div style="text-align: justify">E por último, para que o método showMessageFinPed( ) presente na linha 430 da figura 39 funcione corretamente, é necessário a criação desse atributo presente na imagem, que está ligado com o botão “FINALIZAR PEDIDO” da figura abaixo.
</div>
<p align="center">
  <img src="Print_43.png" />
</p>

_ Botão “FINALIZAR PEDIDO” para finalizar o pedido desejado pelo cliente_ (Figura 43)