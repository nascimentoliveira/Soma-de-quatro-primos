Repositório de programas e scripts utilitários para problemas aplicáveis à Conjectura de Goldbach.

Inspired by Problem #10168 - Summation of Four Primes in

https://onlinejudge.org/external/101/10168.pdf

# Soma de Quatro Primos

Este problema busca transformar qualquer número natural na soma de 4 números primos.

Para encontrar a solução, lançaremos mão da conjectura de Goldbach, que foi proposta pelo matemático prussiano Christian Goldbach.
Trata-se de um dos problemas mais antigos não resolvidos da teoria dos números.

> ***todo número par maior que 2 pode ser representado pela soma de dois números primos.***

Por exemplo: 

* $4 = 2 + 2$;
* $6 = 3 + 3$;
* $8 = 5 + 3$;
* $10 = 3 + 7$;
* $12 = 5 + 7$;
* $14 = 3 + 11$ ou $7 + 7$;
* $16 = 3 + 13$ ou $5 + 11$;
* etc.

Experimentos realizados em computadores já confirmaram a conjectura de Goldbach para muitos números. No entanto, a efetiva demonstração matemática ainda não ocorreu.

Evidentemente, como número $2$ é considerado o menor primo, o menor número que conseguimos tranformar na soma de 4 primos é o $8 = 2 + 2 + 2 + 2$.

Além disso, vale levar em conta o que o teorema de Euclides afirma:

> ***O conjunto dos números primos é infinito.***

Leonhard Euler demonstrou o teorema de Euclides apoiando-se no teorema fundamental da aritmética: 

> ***Cada número tem uma única fatorização prima.***

Se cada número tem uma fatorização prima única, desenvolvemos uma função que encontra todos os fatores primos do número inteiro passado como argumento.

``` {.python}
#Python 3 script to calculate prime factors of N

def factorization(number):

    #unexpected parameter
    if (number < 2 or type(number) != int):
        print("Expected positive values (natural number, starting at 2)!")
        return 

    factors = list()
    divisor = 2

    while (divisor * divisor <= number):
        if (number % divisor == 0):
            number = int(number/divisor)
            factors.append(str(divisor))
        else:
            if (divisor == 2): divisor += 1
            else: divisor += 2
        
    if (number > 1):
        factors.append(str(number))

    return factors
```

``` {.python}
from time import time
inicio = time()

number = 1024
result = factorization(number)

if (result != None):
    print("Prime factors of " + str(number) + ":", ", ".join(result))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
Prime factors of 1024: 2, 2, 2, 2, 2, 2, 2, 2, 2, 2

⏱️ Runtime: 0.00563 seconds.
```

Agora que sabemos os fatores primos de qualquer número natural maior que 1, podemos determinar se ele é um número primo ou não. De maneira simplificada:

> ***Um número primo é todo o número com dois e somente dois divisores, ele próprio e a unidade.***

Trazendo para a nossa implementação, seria o número que contém somente um elemento na sua lista de fatores primos, ele mesmo, já que o divisor 1 não é chamado primo.

Em seguida, uma função que busca a quantidade de fatores primos de determinado número e indica o resultado do seu teste de primalidade.

``` {.python}
#Python 3 script that determines the primality of a number
def isPrime(number):

    #unexpected parameter
    if (number < 2 or type(number) != int):
        print("Expected positive values (natural number, starting at 2)!")
        return

    if (len(factorization(number)) == 1):
        return True
    else:
        return False
```

``` {.python}
from time import time
inicio = time()

number = 97
result = isPrime(number)
if (result != None):
    print("The number " + str(number) + " is", 'prime.' if isPrime(number) else 'not prime.')

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
The number 97 is prime.

⏱️ Runtime: 0.00027 seconds.
```

Agora que já sabemos os fatores primos de qualquer natural maior que 1 e conseguimos determinar se ele é primo, podemos implementar a função que transforma um número na soma de 2 números primos, como Goldbach conjecturou. Lembrando que ser par é hipótese da conjectura.

``` {.python}
#Python 3 script to find two primes that add up to N, for N even
def goldbach(number):
    
    #unexpected parameter
    if (number < 4 or type(number) != int):
        print("Expected positive values (natural number, starting at 4)!")
        return
    
    portion = 2

    while (portion <= number):
        if (isPrime(portion) and isPrime(number - portion)):
            return portion, number - portion 
   
        if (portion == 2): portion += 1
        else: portion += 2
```
``` {.python}
from time import time
inicio = time()

number = 14
result = goldbach(number)
if (result != None):
    print("The number " + str(number) + " is the result of the sum (of the primes) " + str(result[0]) + " + " + str(result[1]) + '.')

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
The number 14  is the result of the sum (of the primes) 3 + 11.

⏱️ Runtime: 0.00198 seconds.
```

Enfim estamos ferramentados com tudo o que precisamos para conseguir resolver o problema principal: transformar um número natural qualquer (chamaremos de $N$), maior que 8, em uma soma de 4 números primos.

Como já sabemos tranformar um número par maior que 2 na soma de 2 primos (Goldbach), basta tranformar o número $N$ em 2 parcela pares quaisquer de uma soma e aplicar a função *goldbach* em ambas as parcela, gerando 4 primos. 

Antes, vamos refletir!

>Um número par é caracterizado pela soma de dois números pares ou pela soma de dois números ímpares.

> Já um número ímpar surge da soma de um número ímpar com um número par.

Então, vamos transformar $N$ em duas parcelas quaisquer de uma soma!

>Se $N$ for par, podemos ter:
>
>1. duas parcela pares; ou
>
>2. duas parcelas ímpares.

>Agora, se $N$ é ímpar, não há outra alternativa a ter:
>
>3. uma parcela ímpar e uma parcela par.

No caso **1** basta aplicarmos a conjectura de Goldbach e encontrar os dois primos para a primeira parcela par e os dois últimos primos da segunda parcela par.

$N = [\text{parcela par}] + [\text{parcela par}]$

$N = [\text{parcela primo} + \text{parcela primo}] + [\text{parcela primo} + \text{parcela primo}]$


Já no caso **2**, basta transferir uma unidade de uma parcela para a outra. Ambas são ímpares. Quando retiro uma unidade de uma parcela, a trasformo em par. Quando adiciono essa unidade na outra parcela, que também era ímpar, ela passa a ser par. Com isso, recaímos no caso **1**.

$N = (\text{parcela ímpar}) + \text{parcela ímpar}$

$N = (\text{parcela par} + 1) + \text{parcela ímpar}$

$N = \text{parcela par} + (1 + \text{parcela ímpar})$

$N = [\text{parcela par}] + [\text{parcela par}]$

$N = [\text{parcela primo} + \text{parcela primo}] + [\text{parcela primo} + \text{parcela primo}]$

A situação **3** requer uma reflexão maior. Temos um número $N$ ímpar que obrigatoriamente tem que ser transformado em uma soma com um fator ímpar e outro par. Olhando pelo lado positivo, já temos uma parcela par, se aplicarmos a função *goldbach* nessa parcela, teremos duas parcelas primos. Mas, e a outra parcela ímpar? 

$N = \text{parcela ímpar} + \text{parcela par}$

Novamente, um número ímpar só pode ser tranformado na soma de uma parcela ímpar com uma par. Mas o único primo par que existe é o $2$. Logo, já conhecemos a primeira parcela primo deste número. A ideia é a seguinte: fixamos a primeira parcela primo, o $2$, e o que restou desta parte da primeira divisão, que é um número ímpar. Vamos retirar 2 unidades dessa parcela impar gerando outra parcela ímpar, duas unidades menor, e tranferindo para a parcela par, gerando outra parcela par, 2 unidades maior.

$N = \text{parcela ímpar} + \text{parcela par}$

$N = 2 + (\text{parcela ímpar} + 2) + \text{parcela par}$

$N = 2 + \text{parcela ímpar} + (2 + \text{parcela par})$

$N = 2 + \text{parcela ímpar} + \text{parcela par}$

... 

Isso se repetirá até que, eventualmente, a parcela ímpar se torne uma parcela primo, e então paramos a tranferência de 2 unidades de uma parcela para outra. Ao final, aplicamos a função de goldbach na parcela par restante para alcançarmos as 4 parcelas primo.

$N = 2 + \text{parcela primo} + [\text{parcela par}]$

$N = 2 + \text{parcela primo} + [\text{parcela primo} + \text{parcela primo}]$


No nosso algoritmo, a primeira divisão de parcelas ocorre na metade de $N$.

$N = N/2 + N/2$, para $N$ par, ou

$N = [N/2 - 0.5] + [N/2 + 0.5]$, para $N$ ímpar

A seguir, a função *fork* que vai dividir o número passado como parâmetro na sua "metade".

``` {.python}
def fork(number):
    if (number % 2 == 0):
        return int(number/2), int(number/2)
    else:
        return int(number/2 - 0.5), int(number/2 + 0.5)
```

Agora, de fato, implementamos tudo o que discutimos:

``` {.python}
#Python 3 script to find 4 prime parcels that add up to a number
def fourPrimes(number):

    if (number < 8 or type(number) != int):
        print("Expected positive values (natural number, starting at 8)!")
        return
    
    parcelTemp1, parcelTemp2 = fork(number)

    parity = (parcelTemp1 % 2) + (parcelTemp2 % 2)

    if (parity == 0):
        prime1, prime2 = goldbach(parcelTemp1)
        prime3, prime4 = goldbach(parcelTemp2)
    
    elif (parity == 2):
        parcelTemp1 += 1
        parcelTemp2 -= 1
        prime1, prime2 = goldbach(parcelTemp1)
        prime3, prime4 = goldbach(parcelTemp2)
    
    else:
        if (parcelTemp1 % 2 == 0):
            evenParcel = parcelTemp1
            oddParcel = parcelTemp2
        else:
            evenParcel = parcelTemp2
            oddParcel = parcelTemp1
    
        while not (isPrime(oddParcel - 2)):
            evenParcel += 2
            oddParcel -= 2
            
        prime1 = 2
        prime2 = oddParcel - prime1
        prime3, prime4 = goldbach(evenParcel)
            
    return [str(prime1), str(prime2), str(prime3), str(prime4)]
```
``` {.python}
from time import time
inicio = time()

number = 5252694
result = fourPrimes(number)
if (result != None):
    print("The number " + str(number) + " is the result of the sum (of the primes)" , " + ".join(result))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")

```
Output:

``` {.python}
The number 5252694 is the result of the sum (of the primes) 29 + 2626319 + 97 + 2626249

⏱️ Runtime: 0.00690 seconds.
```
# Resumo
---

Com esses algoritmos, é possível:

1. Encontrar os fatores primos de um número natural; 
2. Fazer o teste de primalidade de um número natural;
3. Tranformar um número natural par, maior que 2, em uma soma com duas parcelas de números primos;
4. Encontrar 4 parcelas de números primos, que quando somadas, resultam em um número natural, maior que 8;

Implemente os algoritmos acima, troque os parâmetros, teste. Entenda e aprenda.

---

```
"Olhos fixos no caminho, para não errar a direção."
```
