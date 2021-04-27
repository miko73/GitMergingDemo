# ================================
miko oddel
# ================================
4. Opakované výpočty
# ================================

Podmínka while
Podmínky if.. elif.. else
Vnořené podmínky
Příkaz return
Rekurze I
Iterace
Smyčka for..
Funkce range
Funkce enumerate
Funkce filter, map a reduce
Funkce print
Interní index elementu
Glosář
Cvičení
4.1 Podmínka  while
Počítače se často používají k automatickému výpočtu opakujících se úloh. Opakované provádění stejných nebo podobných úloh bez chyb je něco, co počítače dělají lépe než lidé.

Použití příkazu while si ukážeme na funkci countdown:

def countdown(n):           parametr jako počáteční stav počítadla
    while n > 0:            omezující podmínka
        print(n)
        n = n-1             změna stavu počítadla
Příkaz while se dá číst téměř jako prostý text: Pokud bude n > 0, vytiskni hodnotu n a potom ji zmenši o 1. Když se dostaneš k hodnotě n = 0, hodnocení podmínky končí.

Formálněji popíšeme tok výpočtu s příkazem while takto:

Vyhodnoť podmínku while s výstupem False nebo True.
Je-li hodnocení False, vystup ze smyčky while a pokračuj dalším příkazem (pokud existuje).
Je-li hodnocení True, proveď všechny příkazy v těle podmínky a vrať se ke kroku 1.
Tělo podmínky tvoří všechny příkazy pod záhlavím podmínky se stejným odsazením.

Tento typ toku programu se nazývá smyčka, protože se opakovaně vracíme k počátku. Uvědomme si, že když je podmínka nepravdivá již při prvním běhu smyčkou, příkazy uvnitř smyčky se nikdy neprovedou.

Tělo smyčky by mělo měnit hodnotu jedné či více proměnných tak, aby se podmínka nakonec stala nepravdivou a smyčka skončila. Jinak by se opakovala do nekonečna, a byla by to nekonečná smyčka.

V případě funkce countdown(n) můžeme dokázat, že smyčka končí, protože víme, že hodnota n je konečná a že se při každém průchodu smyčkou zmenšuje, takže nakonec se musíme dostat k nule. V jiných případech to tak zřejmé být nemusí.

def sequence(n):
    while n != 1:
        print(n, end=", ")
        if n%2 == 0:         # n je sudé
            n = n//2
        else:
            n = n*3+1
>>> sequence(4)
4, 2,
Podmínkou pro tuto smyčku je n!=1, takže bude rotovat tak dlouho, dokud nebude n=1, čímž se stane podmínka nepravdivá.

Při každém průchodu smyčkou program vrácí hodnotu n a zkontroluje, je-li sudá či lichá. Je-li sudá, je n děleno 2. Je-li lichá, nahradí se hodnotou n*3+1. Například, pro sequence(3) je výsledná posloupnost 3, 10, 5.0, 16.0, 8.0, 4.0, 2.0 .

Protože se n někdy zvětšuje, jindy zmenšuje, nemáme zřejmý důkaz, že n někdy dospěje k 1, nebo že program skončí. Pro jisté hodnoty n můžeme ukončení dokázat. Například, bude-li počáteční hodnotou mocnina 2, bude n stále sudé, dokud nedospěje k 1. V předchozím případě výsledná posloupnost takovou řadu (počínající číslem 16) obsahuje.

Odhlédneme-li od zmíněných čísel, je na místě otázka, zda umíme dokázat, že tento program je konečný pro všechny možné hodnoty n. Zatím se to nikomu nepodařilo!

Jiným příkladem použití smyčky while je traverzování po elementech seznamu:

# Výběr slov se sudým pořadím

slova = ["Copak", "je", "to", "za", "fešáka", "?"]

i = 0
délka = len(slova)
while i < délka :
    if i % 2 == 1 :
        print(slova[i], end=", "")
    i += 1
========== RESTART: F:\Codetest\HowTo\trump.py ==========
je, za, ?,
Následující ukázka demonstruje použití pojmenovaného výrazu (walruss operator) v kombinaci s podmínkou while a vstupem uživatele:

while (user_input := input('Enter q or p: ')) != 'q':
    if user_input == 'p':
        print("Hello!")
========== RESTART: F:\Codetest\HowTo\trump.py ==========
Enter q or p: p
Hello!
Enter q or p: q
>>>

4.2   Podmínky if.. elif.. else
K napsání užitečného programu potřebujeme mít možnost měnit chování programu v závislosti na splnění či nesplnění jistých podmínek.
Tyto podmínky se formulují pomocí relačních (kap. 2.8.2) a logických operátorů (kap. 2.8.3).

4.2.1 Podmínka if..
Tuto jednoduchou podmínku je vhodné použít jako součást jiné procedury, například funkce:

def odmocnina(x):
    if x >= 0:
        print ("odmocnina", x, "=", x**0.5)        # viz odst. 4.11
Stejně jako funkce a jiné složené příkazy se příkaz if skládá ze záhlaví a těla. Záhlaví začíná klíčovým slovem if, pokračuje booleovským výrazem neboli podmínkou a končí dvojtečkou.
Poté, co se podmínka vyhodnotí jako pravdivá, provede se odsazená část složeného příkazu.

>>> odmocnina(5)
odmocnina 5 = 2.23606797749979
4.2.2 Podmínka if .. else
Touto podmínkou realizujeme takzvané alternativní provedení, při němž existují dvě možnosti a podmínka určí, která z nich se provede:

x = int(input("Zadej číslo: "))     # ošetření vstupu z konzoly

if x % 2 == 0:                      # při splnění podmínky
    print (x, "je sudé")            # se provede odsazený příkaz
else:                               # při nesplnění podmínky
    print (x, "je liché")           # se provede tento příkaz
Je-li zbytek po dělení dvěma roven nule, potom víme, že x je sudé a program tuto zprávu zobrazí. Není-li tato podmínka pravdivá, provede se druhá sada příkazů. Protože podmínka může být pouze pravdivá nebo nepravdivá, provede se určitě jedna z obou možností.

Alternativám říkáme větve protože jsou rozvětvením toku programu.

Mimochodem, kdybychom potřebovali často posuzovat "lichost" či "sudost" čísel, mohli bychom si tento prográmek "zabalit" do funkce:
def print_parity(x):
    if x%2 == 0:
        print(x, "je sudé")
    else:
        print(x, "je liché")
Podmínku if .. else lze také uplatnit jako infix mezi dvěma výstupy:

def print_parity(x):
    print(x, " je sudé") if x%2 == 0 else print(x, " je liché")
Pro každou hodnotu x vrátí print_parity příslušnou zprávu. Při volání můžeme zadat jako argument jakýkoliv celočíselný výraz:

>>> print_parity(17)
17 je liché
>>> y = 41
>>> print_parity(y + 1)
42 je sudé
4.2.3 Podmínka if .. elif .. else
Někdy je více než dvě možnosti a my potřebujeme více než dvě větve. Použijeme seriově uspořádané (zřetězené) podmínky:

if x < y:
    print(x, "is less than", y)
elif x > y:
    print(x, "is greater than", y)
else:
    print(x, " and ", y, " are equal")
elif je zkratka "else if". Opět je provedena pouze jedna větev. Počet elif není omezen, příkaz else však smí být pouze jeden a musí být uveden jako poslední.

Podmínky jsou zkoumány jedna za druhou. Je-li první nepravdivá, prověřuje se další. Je-li některá pravdivá, provede se bezprostředně následující větev programu. Jestliže je pravdivých podmínek více, provede se jen první z nich.

4.2.4 Procedure if_case(choice)
Sekvencí podmínek if.., elif.., elif.., else lze simulovat v Pythonu chybějící proceduru switch case. Obdobné řešení pomocí slovníku je uvedeno v Kap. 11.8.

Mějme skript s funkcemi fce_a, fce_b, fce_c a s funkcí if_case(choice):

def fce_a():
    print("fce_a byla volána")
def fce_b():
    print("fce_b byla volána")
def fce_c():
    print("fce_c byla volána")

def if_case(choice):
    if   choice == 'a': fce_a()
    elif choice == 'b': fce_b()
    elif choice == 'c': fce_c()
    else: print("Neplatná volba")
Výstupem v konzole IDLE by mělo být:
===== RESTART: F:\Codetest\HowTo\ch-04\if_case.py =====
>>> if_case("c")
fce_c byla volána
>>> if_case(5)
Neplatná volba

4.3   Vnořené podmínky
Jedna podmínka může být vnořena do druhé. Předchozí trojité větvení můžeme realizovat také takto:

if x == y:
    print(x, "and", y, "are equal")
else:
    if x < y:
        print(x, "is less than", y)
    else:
        print(x, "is greater than", y)
Vnější podmínka má dvě větve. První větev obsahuje prostý příkaz k tisku. Druhá větev obsahuje další podmínku if, která má své vlastní dvě větve. Obě tyto větve jsou prostým voláním funkce print.

I když odsazení příkazů činí strukturu zápisu zřejmou, vnořené podmínky se velmi rychle stávají méně přehledné. Pokud můžeme, tak se jim raději vyhneme.

Vnořené podmínky můžeme často zjednodušit logickými operátory. Následující kód bude v další ukázce přepsán pro použití jen jedné podmínky:

if 0 < x:
    if x < 10:
        print("x is a positive single digit.")
K volání funkce print dojde pouze tehdy, splníme-li obě podmínky, můžeme tedy použít operátor and.

if 0 < x and x < 10:
    print("x is a positive single digit.")
Pro toto docela běžné seskupení podmínek poskytuje Python alternativní syntaxi, která je podobná zápisu v matematice:

if 0 < x < 10:
    print("x is a positive single digit.")
Tato podmínka je významově stejná jako složený booleovský výraz s vnořenou podmínkou.


4.4 Příkaz 'return'
Ve funkci s větvenými podmínkami s výhodou použijeme příkaz return:

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
Protože jsou tyto příkazy v alternativních podmínkách, provedou se pouze jednou - jakmile se jeden z příkazů return provede, funkce končí bez provádění následných příkazů.

Naši funkci můžeme zapsat také stručněji. Místo příkazu else dáme přímo příkaz return.

def absoluteValue(x):
    if x < 0:
        return -x
    return x
Přesvědčme se, že tato fce pracuje stejně jako ta předchozí.

Kód, který je zapsán za příkazem return i kterékoliv další místo, kam se tok programu nedostane, se nazývá mrtvý kód.

Je dobré aby každá možná cesta funkcí narazila na příkaz return. V následující verzi absolute_value toto zajištěno není:

def absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x
Tato verze není zcela správná, protože bude-li x rovno nule, žádná z podmínek není pravdivá a funkce končí, aniž by narazila na příkaz return; výslednou hodnotou je speciální hodnota zvaná None:

>>> print(absoluteValue(0))
None
None je jediná hodnota typu NoneType.


4.5 Rekurze I
Rekurze je technika, při které funkce volá (s jinými parametry) samu sebe . Funkci countdown(n) z odstavce 4.1 můžeme s pomocí rekurze zapsat takto:

def countDown(n):        # základním případem je zde argument n
    if n < 1:            # omezující podmínka
        return
    print(n)
    countDown(n-1)       # rekurzivní volání se změnou argumentu
Správně definovaná rekurze vyhovuje těmto dvěma požadavkům:

Má deklarovaný základní případ u kterého opakovaný výpočet končí. Základní případ je vstupní hodnota posledního volání funkce.
Hodnota argumentu rekurzivního volání směřuje k hodnotě základního případu
Pokud by rekurzivní volání nenarazilo na základní případ, šlo by o nekonečnou rekurzi s neúměrným nárokem na paměť počítače.Tuto situaci si Python sám ošetří tak, že po určitém počtu opakování výpočet zastaví.
V matematice známý pojem faktoriál čísla n neboli n faktoriál: (n!) je označení pro součin souvislé číselné řady 1 až n:
n! = n * (n-1) * (n-2) * ... *1   Ukážeme si jeho různé vyjádření:

Matematická definice:

0! = 1
n! = n(n-1)
Vyjádření pomocí iterace while...

def fact_w(n):
    f, i = 1, 0
    while i < n :
       i = i+1; f = f*i
    return f
Vyjádření pomocí iterace for...

def fact_f(n):
    f = 1
    for i in range(1, n+1):
    f = f*i
    return f
Vyjádření pomocí rekurze

def fact_r(n):
    if n == 0:             # základní případ (případně n < 2 )
        return 1
    return n * fact_r(n-1)
Opakovaný výpočet pomocí rekurze je někdy pomalejší než výpočet pomocí iterace. Na konci odstavce 13.2 si ukážeme výpočet Fibonacciho čísla rekurzí, iterací a rychlý výpočet pomocí memoizace.

Má se za to, že každé rekurzivní řešení lze vyjádřit iterační smyčkou a naopak. Oběma způsobům je společná existence mezní podmínky, určující konec opakovaného výpočtu.
Nekonečná rekurze může skončit krachem systému, zatímco nekonečná iterace je odchycena a ukončena Pythonem.


4.6 Iterace
Pro zvídavé
Iterace obecně je opakování určitého procesu v měnícím se kontextu. V prostředí Pythonu je iterace opakovaný výpočet pro jednotlivé členy iterovatelného objektu prostřednictvím iterátoru.

Iterovatelným objektem (iteráblem) jsou sekvence typu string, list, tuple, range, bytes, bytearray a kolekce typu dict, set, frozentset - rovněž objekty typu file a generátory.

Tyto objekty vlastní funkci iter(~) a metodu __iter__(), které umožňují vytvoření interního objektu, zvaného iterátor.

Iterátor je speciální 'kopie' iterovatelného objektu, disponující funkcí next(~) (a metodou __next__()), která postupně vrací své aktuálně dosažené prvky a vypouští je z 'kopie'. Vypuštění posledního elementu kopie je indikováno sdělením StopIteration.

>>> li = [2, 5, 0]            # iterable

>>> ili = iter(li)            # vytvoření iterátoru
>>> ili = li.__iter__()       # alternativní možnost

>>> next(ili)                 # první krok iterace
2
>>> ili.__next__()            # druhý krok iterace
5
>>> next(ili)                 # poslední krok iterace
0
>>> next(ili)
StopIteration                 # info o konci iterace
Iterátor je v této chvíli prázdný. Opětovně použitelný iterátor vytvoříme opětovným použitím funkce iter(), případně metody  __iter__() :

>>> ili = li.__iter__()
Vlastní iterátor si vytváří idiom FOR a funkce open(), min(), max(), map(), filter(), zip(), enumerate() a reversed().

Iterátory jsou rovněž iterovatelnými objekty (iterábly) ale nemají 'délku' a nelze je indexovat (nedisponují metodou __getitem__()). Jsou výhodné tím, že snižují spotřebu paměti; vyprázdněný iterátor je "garbage collected".

Generátory jsou iterátory, vytvořené generátorovou funkcí, případně generátorovým výrazem. Jsou popsány v kap.13.5, iterátory, definované třídou, jsou popsány v kap. 13.4.


4.7 Smyčka for...
for i in iterable: do something
Smyčka for si pro zadaný iterovatelný objekt (iterable) vytvoří vlastní iterátor, s nímž provádí iteraci po prvcích objektu:

iter_obj = iter(iterable)         # vytvoření vlastního iterátoru

while True:
    try:
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        break                    # konec smyčky
Funkce open("readme.txt") s vlastním iterátorem:

>>> f = open("c:/Abakus/readme.txt")      # iterátor pro readme.txt
>>> next(f)                               # první řádek souboru
>>> next(f)                               # další řádek souboru
>>> for i in f: print(i, end=" ")         # zbývající řádky souboru
st = {3.6, "cat", True}                # kolekce typu set

for i in st:
    print(i, end=" ")
======== RESTART: F:/Codetest/HowTo/trampolina.py ========
True 3.6 cat
>>>
Na výstupu idiomu FOR v konzole IDLE vidíme, že pořadí elementů se změnilo, protože kolekce (set) pořadí měnit může.

Iterace přes slovník (dict) vrací pouze klíče slovníku:

sl = {1: "uno", 2: "duo", 3: "tre"}      # kolekce typu dict

for i in sl:
    print(i, end=" ")
======== RESTART: F:/Codetest/HowTo/trampolina.py ========
1 2 3
>>>
O tom, že naše kontejnery jsou vybaveny metodou __iter__ a že to tedy jsou iteráble, se přesvědčíme funkcí

>>> dir(zkoumaný_objekt)
jejímž výstupem je seznam metod a funkcí zadaného objektu, v němž metodu __iter__ nalezneme.

4.8 Funkce 'range'
Vestavěná funkce range(start, stop[, step]) vytvoří potenciální aritmetickou posloupnost od 0 po n-1, případně od m po n-1, případně od m po n-1 s krokem p. Argumenty start a step jsou nepovinné.
Slovo potenciální označuje tu skutečnost, že místo celé zadané řady čísel se při deklaraci uloží pouze její parametry a k vlastnímu vytvoření této posloupnosti dojde až při jejím volání. Jedná se o případ takzvaného odloženého (lazy) vytvoření iterovatelného objektu (nikoliv jeho iterátoru - viz. odst. 4.6).
Předností funkce range() je skutečnost, že zabírá stejné místo v paměti - bez ohledu na délku deklarované řady.

Tuto posloupnost lze použít jako argument při tvorbě prostého seznamu, entice, setu a sekvence bytes:

>>> list(range (7))              # chápáno jako range(0,7)
[0, 1, 2, 3, 4, 5, 6]
>>> tuple(range (2,7))
(2, 3, 4, 5, 6)
>>> set(range (0,7,2))
{0, 2, 4, 6}
>>> bytes(range (0,7,2))
b'\x00\x02\x04\x06'
>>> list(range (7,5))            # bez vhodného kroku vždy prázdný
[]
>>> list(range (7,0,-3))         # vida
[7, 4, 1]
Objekt typu range je indexovaným (subscriptable) objektem. Jeho elementy jsou individuálně přístupné uvedením indexu v závorce a metodou __getitem__():

>>> range(7)[2]
2
>>> range(7).__getitem__(2)
2
Iterátor lze z objektu range vytvořit běžným způsobem funkcí iter(range) (range.__iter__() ) nebo smyčkou for..., která si iterátor vytvoří sama (sama si jej však také zkonzumuje). Iterace takovéhoto iterátoru je dychtivá (eager - viz  kap. 13.5)

>>> for i in range(7):                 eager iteration
...    print(i, end= ", ")
...
0, 1, 2, 3, 4, 5, 6, >>>
for number in range(20):               eager iteration
    if number%3 == 0:
        print(number, end="  ")
Výstup v IDLE:

======== RESTART: F:/Codetest/HowTo/trampolina.py ========
0  3  6  9  12  15  18
>>>
Poznámka: Takzvanou línou (lazy) iteraci lze provést prostřednictvím funkce range() v komprehenci entice - viz. kap. 8.10.


4.9 Funkce enumerate
Volání funkce enumerate(iterable, start=0) vrací objekt typu enumerate jenž je iterátorem, disponujícím metodou __next__() a funkcí next():

>>> fruits = ('banana', 'apple', 'pear', 'grape')      # iteráble
>>> enum = enumerate(fruits)                           # iterátor
>>> type(enum)                          # --> <class 'enumerate'>
Objekt typu enumerate není indexovatelný (není to iterábl), jeho elementy nejsou přímo přístupné prostřednictvím indexu v hranatých závorkách.

>>> enum[1]
# TypeError: 'enumerate' object is not subscriptable
Přístup k prvkům iterátoru lze realizovat postupně prostřednictvím iterační funkce next nebo smyčky for::

>>> next(enum)
(0, 'banana')
>>> enum.__next__()
(1, 'apple')

>>> for i in enum:
        print(i, end=" ")
(2, 'pear') (3, 'grape')                  # zbytek iterace
Jak vidno, next(enum) i smyčka for vrací index a jemu příslušnou hodnotu. Index implicitně počíná nulou. Počáteční index lze změnit zadáním jiné hodnoty pro parametr start.

Funkci 'enumerate' lze použít pro vyjádření vztahu argument - upravený argument:

numbers = [2, 3, 4, 5]
for elem, value in enumerate(numbers, 1):       # změna hodnoty parametru
    print(elem, numbers[elem], " -> ", value**2)
Výstup v IDLE:

======== RESTART: F:/Codetest/HowTo/trampolina.py ========
1 3 -> 9
2 4 -> 16
3 5 -> 25
...
IndexError: list index out of range
Naše malá záhada: Provedli jsme co jsme měli a přesto nám interpret hlásí chybu. Prosím laskavého čtenáře aby si zkusil sám nalézt příčinu.


4.10 Funkce filter, map a reduce
Všechny tyto tři funkce pracují s iterovatelnými objekty (iterábly - viz 4.6).

Funkce filter ( function or None, iterable ) vrací iterátor, jehož položky jsou filtrovány podle kritéria, zadaného funkcí z argumentu. Jako funkce se často používá anonymní funkce lambda.
Iteráblem může být objekt typu list, string, tuple, set, ...

Výsledný iterátor musíme vhodným způsobem rozbalit (*)

ages = [7, 10, 16, 18, 26, 35]
adults = filter(lambda x: x > 17, ages)

for x in adults:                      * zde idiomem 'for ...'
    print(x, end=" ")

* zde funkcí 'list'
not_adults = list(filter(lambda x: x <= 17, ages))
18 24 32
>>> not_adults
[7, 10, 16]

Funkce map ( fce, iterable, ...) vrací iterátor, jenž aplikuje transformační funkci na každý element iteráblu (seznamu, entice, atp) a vrací výsledek. Iteráblů lze zadat více než jeden.

def squares(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(squares, numbers)
print(list(result))                        --> [1, 4, 9, 16]
Jiný příklad:

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda x,y: x+y, num1, num2)
print(list(result))                        --> [9, 11, 13]

Funkce reduce ( fce, sequence [ , start ] ) vrací jedinou výslednou hodnotu z postupné aplikace dvou po sobě připravených hodnot. Tuto funkci nutno importovat z modulu functools.

from functools import reduce

def do_sum(x, y):
    return x + y

print(reduce(do_sum, [1, 2, 3, 4]))               --> 10

Případně s funkcí lambda:
print(reduce(lambda x,y: x+y , range(1,5)))       --> 10
Funkce 'reduce' v tomto případě postupně provádí součty (((1+2)+3)+4.)


4.11 Funkce print()
Funkce print() se všemi svými parametry má tento tvar:

print(*objekty, sep="", end="\n", file=sys.stdout, flush=False)
Kdo si přečetl odstavec 3.4 Parametry a argumenty II, ví že parametr *objekty je sběrný enticový parametr a všechny ostatní parametry lze ignorovat, neboť to jsou parametry s počáteční hodnotou.
Takže se nám povinný tvar volání funkce smrskne na

print(*objekty)
přičemž i tento parametr lze vynechat a v tom případě nám funkce vytiskne prázdný řádek.
Funkce print vyvolá vyhodnocení jednotlivých argumentů v entici:

>>> print("Je mi", 12 + 9, "let.")
Je mi 21 let.                            # print odebral  "string"
>>>
Klíčové argumenty file=sys.stdout a flush=False zajišťují výstup tisku do okna konzoly.
Změnou argumentu end="\n" na end="" lze zajistit pokračování tisku na témže řádku, přičemž rozestupem uvozovek lze ovlivnit rozestup mezi jednotlivými hodnotami výstupu.
Změnou argumentu sep="" lze přikázat typ oddělovače, případně vzdálenost mezi prvky entice.

>>> print('a', 'b', 'c', 'd')
a b c d
>>> print('a', 'b', 'c', 'd', sep=' # ', end=' !!')
a # b # c # d !!>>>        # prompt '>>>' se vrací pouze v konzole

4.12 Interní index elementu
Všechny sekvence (viz kap. 2.3) jsou takzvaně "indexovatelné" (subscriptable), což znamená že vlastní metodu __getitem__(). Elementy těchto objektů jsou interně indexovány a pomocí těchto indexů jsou přímo dostupné závorkovým operátorem nebo prostřednictvím metody __getitem__():

>>> li = [2, 5, 0]           # 'subscriptable' objekt s indexy 0, 1, 2
>>> li[1]
5
>>> li.__getitem__(1)        # objektem zde je seznam (list)
5
Názornou ilustraci indexování u řetězce představuje tento obrázek:



Poznámka: Grafická interpretace indexování, použitá u tohoto obrázku, se liší od interpretace, použité u obrázku v kap. 6.1. tím, že zde je za indexované místo považován prostor před, mezi a za posledním znakem řetězce, zatímco na obrázku v kap. 6.1 je za indexem označené místo považována přesně pozice znaku. Interpretace v kap. 6.1 je pro naši potřebu vhodnější.

Pomocí záporných čísel se provádí indexování zprava doleva:

>>> fruit[-1]
'a'
>>> fruit[-6]
'b'
>>> fruit[6]
IndexError: string index out of range
Metodu __getitem__() vlastní také objekt typu dict. Jeho elementy jsou podobně přístupné - s tím rozdílem, že jako indexu nutno použít klíč slovníku:

>>> dc = {"m": 5, "n": 6}    # 'subscriptable' objekt s klíči "m", "n"
>>> dc["m"]
5
>>> dc.__getitem__("n")
6
Iterátory objektů (odst. 4.6), přesto, že jsou rovněž iterovatelné, nejsou 'subscriptable' - nepoužívají indexy.


4.13 Glosář
podmíněný příkaz (conditional statement)
Příkaz, který řídí tok výpočtu v závislosti na nějaké podmínce. V Pythonu se pro podmíněné příkazy používají klíčová slova if, elif a   else.
podmínka (condition)
Booleovský výraz v podmíněném výrazu, který rozhoduje o tom, která větev se provede.
řetězená podmínka (chained conditional)
Podmíněné větvení s více než dvěma toky výpočtu. V Pythonu se řetězené podmínky píší pomocí příkazů if ... elif ... else.
větev (branch)
Jedna z možných cest výpočtu určená vyhodnocením podmínky.
iterace (iteration)
Opakované provádění sady programových příkazů
smyčka (loop)
Příkaz nebo skupina příkazů, které se provádějí opakovaně, dokud není splněna ukončující podmínka.
nekonečná smyčka (infinite loop)
Smyčka, ve které ukončující podmínka není nikdy splněna.
proměnná smyčky (loop variable)
Proměnná, jejíž hodnota se mění po každém provedení smyčky.
počítadlo (counter)
Proměnná pro počítání něčeho; obvykle nastavená s nulovou počáteční hodnotou a navyšovaná v těle smyčky.
tělo (body)
Příkazy uvnitř smyčky nebo funkce

4.14 Cvičení
Následující příklady zapisujte do skriptů v IDLE s názvem příslušné funkce. Výstupy spuštěných skriptů se budou postupně realizovat v okně Python Shell.
Všechny příklady zapisujte do samostatných souborů ve složce Kap-04.

Příklady s doctestem budou mít na konci skriptu tento kód:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
Tyto příklady řešte až po prostudování textu v kap. 5.11. Při řešení geometrických úloh pomůže tento vlídný text .

Napište funkci compare(a,b), která vrací 1 pro a>b, 0 pro a==b a -1 pro a<b.
def compare (a, b):
    """
    >>> compare(5,4)
    1
    >>> compare(7,7)
    0
    >>> compare(2,3)
    -1
    """
    # Zde napište tělo funkce
Použijte přírůstkový rozvoj k vytvoření funkce hypotenuse, která vrací délku přepony pravoúhlého trojúhelníka pro zadané délky odvěsen.
Přírůstkové kroky si zkoušejte v samostatné konzole Pythonu, nikoliv v konzole z IDLE. Editační okno a jemu příslušná konzola jsou ovšem z IDLE.
def hypotenuse (a,b):
    """
    >>> hypotenuse(3,4)
    5.0
    >>> hypotenuse(12,5)
    13.0
    >>> hypotenuse(7,24)
    25.0
    """
    # tělo funkce může mít pouhé 2 řádky
Napište funkci slope(x1,y1,x2,y2), která vrací tangent úhlu (sklonu) přímky procházející body (x1,y1) a (x2,y2). Funkce musí vyhovět následujícím testům:
def slope (x1,y1,x2,y2):
    """
    >>> slope(5,3,4,2)
    1.0
    >>> slope(1,2,3,2)
    0.0
    >>> slope(1,4,1,2)
    kolmice k ose 'x'           Ošetřená výjimka!
    >>> slope(2,4,1,2)
    2.0
    """
    # Zde napište tělo funkce
Napište funkci intercept(x1,y1,x2,y2), která vrací ypsilonovou pořadnici průsečíku přímky s osou y (pro x=0). Použijte rovnici přímky, procházející 2 body.

def intercept (x1,y1,x2,y2):
    """
    >>> intercept(1,6,3,12)
    3.0
    >>> intercept(6,1,1,6)
    7.0
    >>> intercept(4,6,12,8)
    5.0
    """
    # Zde napište tělo funkce
Napište funkci is_multiple(m,n), která vrátí True, je-li m násobkem n a False, není-li.
def is_multiple( (m,n):
    """
    >>> is_multiple(12,3)
    True
    >>> is_multiple(12,4)
    True
    >>> is_multiple(12,5)
    False
    """
    # Zde napište tělo funkce
Napište fci is_divisible(m,n), která přijme celá čísla jako argument a podle situace vytiskne True nebo False.

def is_divisible( (m,n):
    """
    >>> is_divisible(20,4)
    True
    >>> is_divisible(21,8)
    False
    """
    # Zde napište tělo funkce
Při řešení použijete podmínky if ... :, else: a vyberete si jeden z existujících způsobů dělení: normální a/b, celočíselné a//b nebo dělení se zbytkem (modulo) a%b.

Napište tělo funkce fah2cel(t), která převede teplotu ve stupních Fahrenheitových na stupně Celsiovy a vrátí ji jako celé číslo. Použijete vestavěnou fci round(n). Informaci o této funkci získáte zadáním >>> round.__doc__ v konzole Pythonu.
def fah2cel(t):
    """
    >>> fah2cel(212)
    100
    >>> fah2cel(32)
    0
    >>> fah2cel(-40)
    -40
    >>> fah2cel(37)
    3
    """
    # Zde napište tělo funkce
Napište funkci cels2fah(t) která převede teplotu ve stupních Celsiových na stupně Fahrenheitovy.
comment up  next how to  end end

# ================================
miko oddel
# ================================
5. Postupy a techniky
# ================================

Zápis běhu programu
Rozvoj programu
Počítání číslic
Tabelární data
Tabulky
Zapouzdření a zobecnění
Další zapouzdření
Další zobecnění
Newtonova metoda
Introspekce Pythonu
Testování s doctestem
Glosář
Cvičení
5.1 Zápis běhu programu
K efektivnímu psaní počítačových programů potřebuje programátor vyvinout schopnost zaznamenat průběh běžícího programu. Znamená to "stát se počítačem" a sledovat průběh provádění, zaznamenávajíc stavy všech proměnných a všechny výstupy, které program generuje po provedení jednotlivých instrukcí.

Abychom porozuměli tomuto procesu, sledujme volání funkce sequence(n) z kapitoly 4.1. Abychom měli tuto funkci na očích, vytvořte v IDLE soubor sequence.py, který si k dalšímu výkladu otevřete.

Průběh volané funkce pro n = 3 si rozepíšeme do tabulky, v níž záhlaví sloupců tvoří jednotlivé výrazy funkce.
V prvním sloupci jsou postupně posuzované hodnoty n, ve třetím sloupci jsou postupně tištěné hodnoty n:

   n     n!=1    print(n)    n%2==0     n/2     n*3+1
  ---    ----    --------    ------    ----    ------
   3       T         3          F        -       10
  10       T        10          T        5        -
   5       T         5          F        -       16
  16       T        16          T        8        -
   8       T         8          T        4        -
   4       T         4          T        2        -
   2       T         2          T        1        -
   1       F         -          -        -        -
Správnost naší sestavy si ověříme spuštěním souboru a voláním funkce pro n=3, jejíž výstup je tento:

>>> sequence(3)
3, 10, 5.0, 16.0, 8.0, 4.0, 2.0,
Provádění záznamu může být únavné a náchylné k chybám, je ale nezbytnou dovedností programátora. Z tohoto záznamu se dozvíme mnohé o tom, jak náš kód pracuje. Můžeme si povšimnout, že jakmile se n stane mocninou 2, potřebuje tělo smyčky log2(n) cyklů ke svému ukončení. Také vidíme, že konečná hodnota 1 se nevytiskne.


5.2 Rozvoj programu
Nyní bychom měli být schopni poznat pouhým pohledem na zápis funkce co má provádět. Pokud jsme prováděli cvičení, sami jsme několik menších funkcí napsali. Při psaní větších funkcí nám mohou nastat potíže kvůli významovým chybám a chybám při běhu programu.

Abychom se vyrovnali s rostoucí složitostí programů seznámíme se s technikou, zvanou přírůstkový rozvoj. Jeho cílem je vyloučení dlouhých seancí při odstraňování chyb tím, že se postupně přidávají a testují krátké úseky kódu.

Jako příklad předpokládejme, že chceme nalézt vzdálenost dvou bodů, daných souřadnicemi (x1, y1) a (x2, y2). Vzdálenost podle Pythagorovy věty je:



Nejprve musíme uvážit jak by měla funkce distance vypadat. Jinými slovy, jaké budou vstupy (parametry) a jaký bude výstup (hodnota return)?

V našem případě musíme na vstupu zadat čtyři souřadnice dvou bodů. Výstupní hodnotou bude jejich vzdálenost s hodnotou typu float.

Již můžeme psát obrys funkce:

def distance(x1, y1, x2, y2):
    return 0.0
Je zřejmé, že tato verze žádnou vzdálenost nepočítá, neboť vždycky vrátí nulu. Je ale skladebně (syntakticky) správná, poběží a můžeme jí testovat před tím než ji zkomplikujeme.

Abychom ji otestovali, zavoláme ji pro jednoduché hodnoty:

>>> distance(1, 2, 4, 6)
0.0
Hodnoty jsme vybrali tak, aby vodorovná vzdálenost bodů byla 3, svislá 4 a výsledná vzdálenost 5 (což je přepona pravoúhlého trojúhelníka). Při testování funkce je užitečné znát správný výsledek předem.

V této chvíli jsme se přesvědčili, že funkce je syntakticky správná a můžeme začít přidávat řádky kódu. Po každé malé změně funkci znovu otestujeme. Objeví-li se v kterémkoli místě chyba, budeme vědět kde musí být – v posledním přidaném řádku.

Prvním logickým krokem ve výpočtu bude nalézt rozdíly x2-x1 a y2-y1. Tyto hodnoty uložíme do dočasných proměnných dx, dy a vytiskneme je.

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is", dx)
    print("dy is", dy)
    return 0.0
Je-li funkce v pořádku, měly by výsledky být 3 a 4. Jestliže ano, ověřili jsme si, že náš dílčí program pracuje správně. Pokud ne, potřebujeme prověřit jenom několik málo řádků.

Nyní sečteme součet čtverců pro dx a dy.

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print("dsquared is: ", dsquared)
    return 0.0
Všimněme si, že jsme odstranili evokace funkce print, které jsme zapsali v předchozím kroku. Takovéto dočasné části kódu říkáme brlení (scaffolding), protože pomáhá při sestavení programu, ale není součástí finálního výsledku.

Opět necháme proběhnout program a zkontrolujeme výstup (což by mělo být 25).

Konečně, s použitím zlomkového exponentu 0.5 pro nalezení odmocniny, můžeme spočítat výsledek:

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result
Pokud nám to chodí správně, jsme hotovi.

Když začínáme, měli bychom přidávat jen po jednom či dvou řádcích. Po získání jisté zkušenosti můžeme přidávat po větších dávkách. Přírůstkový rozvoj nám v každém případě ušetří mnoho času při odstraňování chyb.

Klíčové aspekty tohoto postupu jsou:

Začneme s fungujícím programem a děláme malé přírůstkové změny. V každém okamžiku víme přesně kde může být případná chyba.
Použijeme dočasných proměnných k uložení mezivýsledků, takže je můžeme vytisknout a zkontrolovat.
Když program pracuje bezchybně, můžeme odstranit nepotřebné brlení, případně uspořádat některé příkazy do složených výrazů, ovšem tak, aby program zůstal dostatečně přehledný.
Stejný tvar funkce pro určení vzdálenosti dvou bodů jsme vytvořili již v kapitole 3.8:

import math
def distance(x1,y1, x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

5.3 Počítání číslic
Následující funkce spočítá počet číslic kladného celého čísla (>= 0):

def num_digits(n):
    if n == 0: return 1     # specielní případ

    count = 0               # počítadlo
    while n:
        count += 1
        n = n//10           # celočíselné dělení
    return count
Volání num_digits(710) vrátí 3. V rámci cvičení (13.6) si tuto funkci upravíme pro všechna celá čísla.

V této funkci vidíme často používaný objekt, zvaný počítadlo (count). Proměnná count je zavedena s hodnotou 0 a potom zvětšována o 1 při každém splnění podmínky smyčky. Když smyčka skončí, obsahuje count celkový počet splnění podmínek, což je zde počet číslic zadaného čísla.
Postupně prováděné celočíselné dělení vypouští poslední číslici zadaného čísla.

Kdybychom chtěli počítat jenom číslice 0 nebo 5, pomůžeme si rozšířením podmínky před zvyšováním stavu počítadla:

def num_0_and_5_digits(n):
    if n == 0: return 1             # nula je také číslice

    n = abs(n)
    count = 0                       # počítadlo
    while n:
        zbytek = n%10               # další pomocná proměnná
        if zbytek == 0 or zbytek == 5:
            count = count+1         # případně count += 1
        n = n//10                   # celočíselné dělení
    return count
Přesvědčte se, že  num_0o_and_5_digits(1055030250) vrací 7.

5.4 Tabelární data
Jedním z vhodných použití smyčky je generování tabelárních dat. Předtím, než byly počítače běžně přístupné, musely být logaritmy, siny, kosiny a jiné funkce čísel počítány ručně. Pro ulehčení výpočtu obsahovaly matematické příručky dlouhé tabulky s uspořádanými hodnotami těchto funkcí. Vytváření tabulek bylo zdlouhavé, nudné a občas plné chyb.

Když se na scéně objevily počítače, jedna z prvních reakcí byla: "Sláva! Můžeme tvořit tabulky na počítači, který nedělá chyby." To se ukázalo být (většinou) pravdivé, ale i krátkozraké. Brzy nato se staly kalkulátory a počítače tak všudepřítomné, že se tabulky staly zbytečné.

Tedy téměř. Pro některé operace používají počítače tabulky hodnot jako přibližnou mezihodnotu, kterou potom v dalším výpočtu upřesňují. Někdy byly chybné právě tyto tabulky; nejproslulejší jsou ty, které Intel Pentium používal k výpočtu dělení v plovoucí řádové čárce.

Při sestavování tabulek se prováděly opakované výpočty pro monotónně měněné vstupní hodnoty. Příkladem opakovaného výpočtu budiž následující program, který vytvoří posloupnost hodnot v levém sloupci a příslušné mocniny čísla 2 v pravém:

x = 1
while x < 13:
    print(x, '\t', 2**x)
    x += 1
Řetězec '\t' zastupuje znak tab, neboli tabulátor. Zpětné lomítko označuje začátek "escape" sekvence, což je pořadí několika určených znaků, které nahrazují neviditelné znaky např. pro tab nebo nový řádek ('\n').

"Escape" sekvence se může použít kdekoliv v řetězci; v našem příkladě je v řetězci pouze znak pro tab. (Jak zapíšeme zpětné lomítko v řetězci?)

Jak jsou postupně znaky a řetězce zobrazovány na obrazovce, jsou kontrolovány neviditelným hlídačem, zvaným kurzor, který zaznamenává jejich polohu.

Znak pro tabulátor posune kurzor doprava k nejbližší pomyslné zarážce. Tabulátory jsou vhodné pro tvorbu uspořádaných řádků, jako má tento výstup z předchozího programu:

>>>
1       2
2       4
3       8
4       16
5       32
6       64
7       128
8       256
9       512
10      1024
11      2048
12      4096
>>>
Protože mezi sloupci máme znaky tab, není pozice druhého sloupce závislá na počtu číslic v prvním sloupci.


5.5 Tabulky
Tabulka je uspořádání údajů, ve kterém je odečítáme v průsečíku řádku a sloupce. Dobrým příkladem je tabulka násobení. Řekněmež, že chceme zobrazit tabulku pro násobení čísel od 1 do 6.

Dobrým začátkem je zápis smyčky, která vytiskne všechny násobky dvou na jeden řádek:

i = 1
while i <= 6:
    print(2*i, "\t", end="")
    i += 1
print()
První řádek vytvoří proměnnou i, která působí jako počítadlo, neboli proměnnou smyčky. Při procházení smyčkou se hodnota i zvětšuje od 1 do 6. Při každém průchodu se vytiskne hodnota 2*i, následovaná mezerou tabelátoru.

Přechod na nový řádek ve funkci print potlačí instrukce end=" ". Po ukončení smyčky vytiskne funkce print() nový řádek.

Výstup programu je tento:

>>>
2   4   6   8   10   12
>>>
Výborně, jen tak dál. Dalším krokem bude zapouzdření a generalizace.


5.6 Zapouzdření a zobecnění
Zapouzdření je proces zabalení kódu do funkce, umožňující jeho snadné opakované použití. Příklad zapouzdření jsme viděli v části   4.2.2 :   print_parity.

Zobecněním se míní přetvoření určité funkce, jako je například tvorba násobků dvou, tak aby tiskla násobky jakéhokoliv čísla.

Následující funkce zapouzdří předchozí smyčku a zobecní ji tak aby vracela násobky  n.

def print_multiples(n):
    i = 1
    while i <= 6:
        print(n*i, "\t", end="")
        i += 1
    print()
Všechno, co jsme pro zapouzdření museli udělat bylo to, že jsme přidali záhlaví funkce s parametrem  n.

Zavoláme-li tuto funkci pro argument 2, dostaneme stejný výstup jako předtím. Pro argument 3 obdržíme:

>>>
3    6    9    12   15   18
>>>
Pro argument 4 je výstup:

>>>
4    8    12    16   20   24
>>>
Nyní patrně už umíme odhadnout jak vytvořit tabulku pro násobení - opakovaným voláním print_multiples pro různé argumenty. Vlastně můžeme použít ještě jednu smyčku:

i = 1
while i <= 6:
    print_multiples(i)
    i += 1
Všimněme si, jak podobná je tato smyčka té, která je uvnitř print_multiples. Výměna funkce print voláním funkce print_multiples bylo vše, co jsme učinili.

Výstup tohoto programu je tabulka pro vzájemné násobení čísel 1- 6 :

>>>
1    2    3     4    5    6
2    4    6     8    10   12
3    6    9     12   15   18
4    8    12    16   20   24
5    10   15    20   25   30
6    12   18    24   30   36
>>>

5.7 Další zapouzdření
Abychom si ještě jednou předvedli zapouzdření, vezměme kód z předcházejícího odstavce a zabalme jej do funkce:

def print_mult_table():
    i = 1
    while i <= 6:
        print_multiples(i)
        i += 1
Tento proces je běžná rozvojová metoda. Vytvářený kód zapisujeme do řádků mimo funkci, případně jej zkoušíme v IDLE či konzole interpreta. Jakmile nám chodí, zabalíme jej do funkce.

Tato metoda je zvláště užitečná, když na počátku ještě nevíme, jak program do funkcí rozdělit. Program tak vzniká postupným vývojem.


5.8 Další zobecnění
Pro další příklad zobecnění předpokládejme, že chceme program, který by vytiskl tabulku násobení jakékoliv velikosti, nikoliv pouze šest krát šest. Můžeme přidat parametr do funkce print_mult_table:

def print_mult_table(high):
    i = 1
    while i <= high:
         print_multiples(i)
         i = i + 1
Hodnotu 6 jsme nahradili parametrem high. Zavoláme-li print_mult_table(7), zobrazí se:

>>>
1    2    3    4    5    6
2    4    6    8    10   12
3    6    9    12   15   18
4    8    12   16   20   24
5    10   15   20   25   30
6    12   18   24   30   36
7    14   21   28   35   42
>>>
To je prima, až na to, že asi chceme, aby byla tabulka čtvercová - se stejným počtem řádků jako sloupců. Zajistíme to přidáním dalšího parametru do print_multiples abychom určili, kolik sloupců by tabulka měla mít.

Tento parametr schválně nazveme high, abychom předvedli, že různé funkce mohou mít parametr se stejným jménem (stejně jako lokální proměnné). Zde je celý program:

def print_multiples(n,high):
    i = 1
    while i <= high:
        print(n*i, "\t", end="")
        i += 1
    print()

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i, high)
        i += 1
Povšimněme si, že s přidáním nového parametru jsme museli změnit první řádek funkce (záhlaví funkce), a také jsme museli změnit místo, kde je funkce v print_mult_table volána.

Dle očekávání generuje program čtvercovou tabulku 7x7:

>>>
1    2    3    4    5    6    7
2    4    6    8    10   12   14
3    6    9    12   15   18   21
4    8    12   16   20   24   28
5    10   15   20   25   30   35
6    12   18   24   30   36   42
7    14   21   28   35   42   49
>>>
Provedeme-li zobecnění vhodným způsobem, často dostaneme program se schopnostmi, které jsme nezamýšleli. Například si lze všimnout, že v důsledku toho, že ab = ba, všechny hodnoty se v tabulce opakují dvakrát. Mohli bychom ušetřit inkoust kdybychom tiskli jen polovinu tabulky. Zařídíme to pouhou změnou jednoho řádku v print_mult_table. Změňme

print_multiples(i, high)
na

print_multiples(i, i)
a obdržíme

>>>
1
2    4
3    6    9
4    8    12   16
5    10   15   20   25
6    12   18   24   30   36
7    14   21   28   35   42   49
>>>

5.9 Newtonova metoda
Smyčky jsou často užívány v programech, které spočítají výsledek tak, že začnou s přibližnou hodnotou a opakovaným výpočtem výsledek zpřesňují.

Například, jedním ze způsobů počítání druhé odmocniny čísla je Newtonova metoda. Při určení odmocniny čísla n začneme vpodstatě libovolnou aproximací (přibližnou hodnotou), kterou zpřesníme pomocí tohoto vzorce:

better = (approx + n/approx)/2
Výpočet se opakuje tak dlouho, až se zpřesněná hodnota téměř neliší od předchozí. Pro provádění výpočtu napíšeme funkci:

def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
    return approx
Volejme funkci pro argument 25, abychom se přesvědčili, že výsledek je 5.0.
Newtonova metoda je příkladem algoritmu - obecného řešení určitého problému (v našem případě počítání druhé odmocniny).


5.10 Introspekce Pythonu
Introspekce Pythonu je akt zkoumání obsahu a vlastností jednotlivých jeho objektů. Za tímto účelem disponuje Python řadou vestavěných funkcí, z nichž některé již známe.

type(obj)     Vrací typ (třídu) objektu
id(obj)         Vrací identifikační číslo objektu
dir(obj)     Vrací seznam metod a atributů objektu. Funkce dir() vrací jména aktuálního prostoru konzoly:
>>> omen = "Alenka"
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__',
 '__name__', '__package__',  '__spec__', 'omen', 'sys']
isinstance(obj, class)     Ověří, zda je objekt instancí zadané třídy.
>>> isinstance(5, int)
True
getattr(obj, "atrib")     Vrací obsah zadaného atributu.
>>> getattr(omen, "__doc__")
"str(object='') -> str\nstr(bytes_or_buffer[, ...
... sys.getdefaultencoding().\nerrors defaults to 'strict'."

5.11 Testování s 'doctestem'
Při rozvoji programu se s oblibou provádí testování vybraných úseků zdrojového kódu. Pro toto testování poskytuje Python moduly doctest a unittest.

Popíšeme si práci s modulem doctest. Zkoumané vzorky kódu se umístí do dokumentačního řetězce pod záhlavím funkce. V každém vzorku je na prvním řádku kód, jakoby zadaný v interaktivním režimu, na druhém řádku je očekávaná odezva.

Modul doctest automaticky spustí příkaz začínající >>> a jeho výstup porovná s následujícím řádkem.

Následující ukázku si uložte do souboru ch05_doctest.py, který spustíte z příkazového řádku konzoly:

# ch05_doctest.py

def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    """

    return n % 2 == 0 or n % 5 == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
Poslední tři řádky spouští celou parádu. Umisťujeme je na konec každého souboru, který obsahuje doctesty.

Pokud procedura zjistí shodu mezi zkoumanými vzorky a zadanými výsledky, reaguje "mlčením". Pokud narazí na rozpor, spustí rozsáhlé chybové hlášení, zejména doplníme-li evokaci skriptu atributem -v (verbose).

Spuštění neúspěšného skriptu vyprodukuje například následující výstup:

> python ch05_doctest.py
******************************************************************
File "ch05_doctest.py", line 3, in __main__.is_divisible_by_2_or_5
Failed example:
    is_divisible_by_2_or_5(8)
Expected:
    True
Got nothing
******************************************************************
1 items had failures:
   1 of   1 in __main__.is_divisible_by_2_or_5
***Test Failed*** 1 failures.

5.12 Glosář
přírůstkový rozvoj (incremental development)
Postupné rozšiřování programu se záměrem testovat postupně jenom menší objem kódu.
brlení (scaffolding)
Kód, použitý při rozvoji programu, který není součástí konečné verze.
záznam (trace)
Sledování toku výpočtu, při kterém se zaznamenávají hodnoty proměnných a výstupů.
zpětný záznam (traceback)
Seznam prováděných funkcí, který se zobrazí na obrazovce, když se vyskytne chyba při běhu programu. Zpětný záznam je také uváděn jako záznam zásobníku, protože probírá funkce v pořadí, ve kterém byly do zásobníku běhu programu zařazeny (runtime stack).
zapouzdřit (encapsulate)
Zabalit část programu do funkce.
rozvojová metoda
Postup vývoje programu. V této kapitole jsme si předvedli způsob, založený na vytváření kódů pro jednoduché, specifické úkoly; kódy jsou potom zapouzdřeny a generalizovány.
 jednotkové testování (unit testing)
Automatická procedura používaná k ověření správné činnosti jednotlivých úseků kódu. V Pythonu se pro tento účel používá vestavěný modul doctest.

5.13 Cvičení
Napište jediný řetězec, který
 stvoří
 tento
 výstup
Přidejte volání funkce print k fci sqrt definované v odstavci 5.9 tak, že vytiskne hodnotu better ve smyčce po každé aproximaci. Volejte upravenou funkci pro argument 25 a zapište výsledky.
Zaznamenejte průběh výpočtu poslední verze fce print_mult_table (odstavec 5.8) a zamyslete se nad jeho postupem.
Do souboru triangularNumbers.py napište funkci print_triangular_numbers(n), která vytiskne součet prvních n členů aritmetické posloupnosti (1 3 6 10 ... trojúhelníková čísla). Voláním funkce dostaneme následující výstupy:
 1     1
 2     3
 3     6
 4     10
 5     15
Do souboru testPrime.py vložte funkci test_prime, která vyhodnotí zadané celé číslo a vrátí True pro argument, který je prvočíslem a False pro argument, který prvočíslem není. Při vývoji funkce používejte "doctesty".
Soubor s doctesty končí tímto kódem:
if __name__ == '__main__':
    import doctest
    doctest.testmod()
Funkce num_digits(n) v odstavci 5.3 nepracuje správně pro n < 0. Doplňte ji tak, aby pracovala správně pro všechna celá čísla (včetně nuly).

def num_digits(n):
    """
    >>> num_digits(12345)
    5
    >>> num_digits(0)
    1
    >>> num_digits(-12345)
    5
    """
Do souboru numEvenDigits.py přidejte následující kód a tělo příslušné funkce:
def num_even_digits(n):
    """
    >>> num_even_digits(123456)
    3
    >>> num_even_digits(2468)
    4
    >>> num_even_digits(1357)
    0
    >>> num_even_digits(2)
    1
    >>> num_even_digits(20)
    2
    """
Do souboru printRevDigits.py přidejte následující kód a tělo přislušné funkce:
def print_digits(n):
    """
    >>> print_digits(13789)
    9 8 7 3 1
    >>> print_digits(39874613)
    3 1 6 4 7 8 9 3
    >>> print_digits(213141)
    1 4 1 3 1 2
    """
Nutno zajistit, aby mezi číslicemi výstupu byly mezery a aby za poslední číslicí žádná mezera nebyla. Numerický argument funkce nutno před manipulací přetvořit na string (viz 2.6), jehož délku určíme funkcí len (viz 2.10).
Pokud se vám nepodaří aby za poslední číslicí žádná mezera nebyla, nevyjádří doctest souhlas mlčením. Jednotlivá funkce ale může pracovat bez závady - protože mezera za poslední číslicí jinak nevadí.
Do souboru sumofSquares.py přidejte funkci sum_of_squares(n), která spočítá součet čtverců číslic zadaného celého čísla. Například, sum_of_squares(72) by mělo vrátit 53, protože 7**2 + 2**2 == 49 + 4 == 53.
def sum_of_squares_of_digits(n):
    """
    >>> sum_of_squares(1)
    1
    >>> sum_of_squares(9)
    81
    >>> sum_of_squares(11)
    2
    >>> sum_of_squares(121)
    6
    >>> sum_of_squares(987)
    194
    """
Svá řešení ověřte pomocí doctestů.

# ================================
miko oddel
# ================================
6. Řetězce
# ================================

Složený datový typ
Úseky řetězce
Délka řetězce
Řetězce jsou neměnitelné
Operace s řetězci
Modul 'string'
Smyčka 'while' a 'for'
Příkaz 'break'
Příkaz 'continue'
Operátor 'in' a 'not in'
Porovnávání řetězců
Použití metod
Sestavení funkce 'find'
Formátování řetězců I
Formátování řetězců II
Formátování řetězců III
Dokumentační řetězce
Glosář
Cvičení

6.1 Složený datový typ
Řetězce (strings) jsou neměnitelné sekvence znaků Unicode, vymezené uvozovkami - jednoduchými, dvojitými či trojitými.
Výraz "bim" "bam" je automaticky konvertován na "bim bam".

Pořadí znaku v řetězci je interně indexováno zleva i zprava, neboli je vyjádřeno pořadovým číslem, které zleva začíná nulou.


Při indexování v opačném směru začíná indexování zápornou jedničkou (-1) na posledním místě řetězce vpravo. Hranaté závorky slouží jako operátor, který vybere indexem určený znak z řetězce.

>>> tuto = "Hello World"

>>> print(tuto[1])
e
>>> print(tuto[-1])
d

6.2 Úseky řetězce
Část řetězce se nazývá úsek (slice). Výběr úseku se provádí úsekovým operátorem. Operátor [n:m] vrací úsek řetězce od znaku n včetně po znak před m. :

>>> s = "Peter, Paul, and Mary"
>>> print(s[0:5] )                    # od 0 po 4 včetně (před 5)
Peter
>>> print(s[7:11])                    # od 7 po 10 včetně (před 11)
Paul
>>> print(s[17:21])
Mary
Vynecháme-li první index (před dvojtečkou), začíná úsek na počátku řetězce. Vynecháme-li druhý index, úsek jde až ke konci řetězce. Takže:

>>> fruit = "banana"
>>> fruit[:3]                         # od 0 po 2 včetně
'ban'
>>> fruit[3:]                         # od 3 do konce
'ana'
Výběr úseku se zadaným odstupem prvků zařídíme úsekovým operátorem se třemi parametry [m:n:k]. Ten je vždy implicitně přítomný s krokem k=1.

>>> tuto = "buttons"
>>> tuto[::2]                         # k = 2
'btos'
>>> print(tuto[::-2])                 # funkce print "očistí" výstup
sotb
Operátor [:] vrací celý řetězec, operátor [::-1] vrací obrácené pořadí řetězce, číslo -1 je třetím parametrem k.

>>> tuto[:]
buttons
>>> tuto[::-1]
snottub
>>> tuto[1:6:2]
'utn'

6.3 Délka řetězce
Funkce len vrací počet znaků v řetězci:

>>> fruit = "banana"
>>> len(fruit)
6
Ve snaze získat poslední písmeno řetězce bychom mohli být v pokušení zkusit něco jako:

>>> délka = len(fruit)
>>> last = fruit[délka]
IndexError: string index out of range
>>> last = fruit[délka-1]
a

6.4 Řetězce jsou neměnitelné
Může být lákavé použít výběrový operátor [] na levé straně přiřazení se záměrem změnit znak v řetězci. Například:

greeting = "Hello, world!"
greeting[0] ='J'        # chyba!
print(greeting)
Místo výstupu Jello, world!, tento kód způsobí chybu při běhu programu: TypeError: 'str' object doesn´t support item assignment.

Řetězce jsou neměnitelné, což znamená, že existující řetězec nelze změnit. Jediná věc, kterou lze udělat, je vytvořit nový řetězec, který je variací původního:

greeting = "Hello, world!"
new_greeting = greeting[:5] + " all" + greeting[6:]
print(new_greeting)
'Hello all world!'
Řešením je zřetězení vložené části s úseky řetězce greeting. Tato operace nemá žádný vliv na původní řetězec.


6.5 Operace s řetězci
6.5.1 Společné operace pro řetězce, entice a seznamy
Obecně vzato, na řetězcích nelze provádět matematické operace. Následující výrazy nejsou přípustné :

"uno" - 1   "Hello / 123   "duo" * "Hello"   "15" + 2
Operátor + však s řetězci pracovat umí, i když jinak, než bychom očekávali. Pro řetězce, entice a seznamy představuje operátor + příkaz zřetězení (concatenation), což je spojení dvou operandů jejich připojením těsně k sobě. Například:

>>> "Chléb " + " a hry"
Chléb a hry
>>> 1, 2, 3, + 4, 5, 6,    # oba operandy jsou entice
(1, 2, 3, 4, 5, 6)
>>> 1, 2, 3 + 4, 5, 6
(1, 2, 7, 5, 6)            # spojení neúplných entic
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
Operátor * rovněž pracuje s řetězci, enticemi i seznamy, způsobuje jejich zmnožení. Jeden z operandů musí být sekvence, druhým operandem musí být celé číslo, například:

>>> 3 * "bla " == "bla " * 3 == "bla bla bla "
True
>>> (1, 2, 3) * 3              jen v závorkách!
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

6.5.2 Volně přístupné metody pro řetězce
Kromě společných procedur pro řetězce a seznamy existuje také velké množství vestavěných metod, speciálně určených pro řetězce, které většinou evokujeme sestavou  'řetězec'.metoda():

  capitalize, casefold, center, count, encode, endswith, expandtabs,
  find, format, format_map, index, isalnum, isalpha, isdecimal,
  isdigit, isidentifier, islower, isnumeric, isprintable, isspace,
  istitle, isupper, join, ljust, lower, lstrip, maketrans, partition,
  replace, rfind, rindex, rjust, rpartition, rsplit, rstrip,
  split, splitlines, startswith, strip, swapcase, title, translate,
  upper, zfill
Metody join a split jsou popsány v Kap. 9.1.


6.5.3 Zdroje informací
Potřebné parametry při volání jednotlivých metod naleznete na stránce String Methods, případně lze číst dokumentační řetězec z definice metody příkazem (například):

>>> print( "".find.__doc__)                  # ověřte si to
V prostředí PyScripter se tyto termíny zobrazují jako nápověda včetně požadované skladby a stručného popisu:

pic
Z výše uvedeného obrázku je patrné, že pro objekt s = "Růžový kavalír" má být tečkovou notací volána nějaká metoda. Tuto metodu lze zapsat do konzoly nebo vybrat z automaticky otevřeného seznamu.


6.6 Modul 'string'
Modul string obsahuje další užitečné objekty pro manipulaci s řetězci. Jako obvykle, modul musíme importovat dřív než jej použijeme:

>>> import  string
Obsah modulu zjistíme vestavěnou fcí dir se jménem modulu jako argument:

>>> dir(string)
čímž dostaneme seznam atributů:
[ 'ascii_letters', ascii_lowercase', ascii_uppercase', digits', hexdigits', 'octdigits', printable', punctuation', 'whitespace' ]
a specielních metod:

['Formatter', 'Template', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__','__package__', '_re', '__spec__', '_sentinel_dict', '_string', 'capwords']
Udělejte si průzkum a sami si zjistěte, co jednotlivé atributy vracejí:

>>> string.digits
'0123456789'

>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

>>> string.whitespace
' \t\n\r\x0b\x0c'                escape sekvence pro whitespace
Znaky whitespace posouvají kurzor, aniž by se cokoli tisklo. Vytvářejí prázdné místo mezi viditelnými znaky.

Konstanty lze s výhodou použít v různých ověřovacích funkcích, například:

def is_lower(ch):
    return string.ascii_lowercase.find(ch) != -1
Nutno si uvědomit, že tato funkce neodpovídá na otázku, zda zkoumané písmeno je velké či malé ale zda patří do sady ascii_lowercase (kde se písmeno "ch" nevyskytuje - stejně jako česká písmena s diakritikou).

>>> is_lower("ch")
False
Metoda string.capwords(str [, sep=None]) rozdělí řetězec na jednotlivá slova (podle zadaného separátoru), počáteční písmena nahradí velkými a znovu spojí jednotlivá slova do jednoho řetězce. Použije-li se jako separátor znak, který není v původním řetězci obsažen, metoda vrátí řetězec s malými písmeny. Bez separátoru odstraní přebytečné mezery

>>> string.capwords("Honolulu  ", "o")
'HoNoLulu  '
>>> string.capwords("    Hono Lu  lU", "čau")
'    hono lu  lu'
>>> string.capwords("  Honolulu    ")
'Honolulu'

6.7 Smyčka 'while' a 'for'
Opakovaný výpočet pro jednotlivé elementy řetězce lze s výhodou provést pomocí smyčky while (viz 4.1):

fruit = "banana"
index = 0                              # počáteční stav počítadla
while index  <  len(fruit):            # podmínka
    letter = fruit[index]
    print(letter, end=" ")
    index = index + 1                  # změna stavu počítadla
========== RESTART: F:\Codetest\HowTo\trump.py ==========
b a n a n a
>>>
Tato smyčka prochází řetězcem a vytiskne každé písmeno. Podmínka smyčky je index < len(fruit), protože index počíná nulou a jeho maximální hodnota je len(fruit)-1.

Komfortnějším nástrojem k procházení (traverzování) iterovatelným objektem je smyčka for:

for char in fruit:
    print(char, end=" ")
Na rozdíl od smyčky while ... používá smyčka for ... k procházení objektem interní objekt, zvaný iterátor - viz kap. 4.7.

Následující příklad ukazuje použití zřetězení (concatenation) a smyčku for pro tvorbu abecedních řad. Abecedním je míněno uspořádání prvků řady či seznamu podle abecedy. Například, v knize Roberta McCloskeyho: Uvolněte cestu pro káčata se kachňata jmenují: Jack, Kack, Lack, Mack, Nack, Ouack, Pack a Quack. Tato smyčka vydá jejich jména v pořadí:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix, end=" ")
Výstup programu je tento:

Jack  Kack  Lack  Mack  Nack  Oack  Pack  Qack
V pořádku to úplně není, protože Ouack a Quack nejsou zapsáni správně. Tuto chybu napravíme v rámci cvičení 6.19.1.


6.8 Příkaz 'break'
Při splnění podmínky ukončí příkaz break provádění smyčky. Tento příkaz lze použít u smyček for  i  while:

for letter in "Python":
    if letter == "h":
        break
    print("Current Letter: ", letter)
Current Letter:  P
Current Letter:  y
Current Letter:  t
nebo:

var = 8
while var > 0:
    print("Current var. value: ", var)
    var = var - 1
    if var == 5:
        break
print("Adieu!")
Current var. value:  8
Current var. value:  7
Current var. value:  6
Adieu!

6.9 Příkaz 'continue'
Při splnění podmínky přeruší příkaz continue provádění smyčky a její výpočet pokračuje dalším elementem sekvence. Tento příkaz lze použít u smyček for i while:

for letter in "Python":
    if letter == "h":
    print("        Jsme přerušeni!")
        continue
    print("Current Letter: ", letter)
Current Letter:  P
Current Letter:  y
Current Letter:  t
        Jsme přerušeni!
Current Letter:  o
Current Letter:  n
nebo:

var = 6
while var > 0:
    var = var - 1
    if var == 3:
    print("        Jsme přerušeni!")
        continue
    print("Current var. value: ", var)
print("Adieu!")
Current var. value:  5
Current var. value:  4
        Jsme přerušeni!
Current var. value:  2
Current var. value:  1
Current var. value:  0
Adieu!

6.10 Operátor 'in' a 'not in'
Operátor in, not in přezkoumá, zda je zadaný řetězec součástí jiného:

>>> 'p' in 'apple'
True
>>> 'i' in 'apple'
False
>>> 'ap' not in 'apple'
False
>>> 'pa' not in 'apple'
True
Všimněme si, že řetězec může být součástí sebe sama:
>>> 'a' in 'a'
True
>>> 'apple' in 'apple'
True
Použitím operátoru in a zřetězení můžeme napsat funkci, která odstraní všechny samohlásky z řetězce:

def remove_vowels(str):
    samohl = "aeiouyAEIOUY"
    str_bez_samohl = ""             # akumulátor
    for letter in str:
        if letter not in samohl:
            str_bez_samohl += letter
    return str_bez_samohl
Prázdný objekt, označený jako akumulátor, je kontejner (zde řetězec) s rozšiřujícím se obsahem.
Podobným objektem je počítadlo, kde se mění jen počáteční stav čísla.


6.11 Porovnávání řetězců
Při porovnávání řetězců se porovnávají kódová čísla znaků se stejným indexem. Postupuje se zleva doprava.

Rovnost řetězců zjistíme:

word = "Zebra"
if word == "banana":
   print ("Ano, banány máme!")
print("Žádný takový!")
Jiné relační operátory jsou užitečné při uspořádávání slov podle abecedy:

if word < "banana":
   print("Your word, " + word + ", comes before banana.")
elif word > "banana":
   print("Your word, " + word + ", comes after banana.")
else:
   print("Maybe, we have bananas!")
Musíme si však být vědomi toho, že Python řadí velká písmena (v důsledku svých číselných hodnot) před malá, proto:

Your word, Zebra, comes before banana.
Souvislost znaku s číselnou hodnotou nám také umožňuje použít funkce min(), max(), ord() a chr():

>>> min("žoužel"), max("žoužel")
('e', 'ž')
>>> ord(min("žoužel")), ord(max("žoužel"))
(101, 382)
>>> chr(101), chr(382)
('e', 'ž')

6.12 Použití metod
Řetězce jsou sice neměnitelné ale lze libovolně upravovat jejich (často interně vytvářené) kopie. Pro tento účel existuje řada funkcí a metod.

Metoda '.removeprefix/suffix()'
Těmito metodami lze změnit začátek a konec řetězce:

>>> "some Text".removeprefix("some ")
'Text'
>>> "some Text".removesuffix("Text")
'some '
Metoda '.replace()'
Tato metoda string.replace(old, new [,count]) vytvoří kopii zadaného řetězce, v němž nahradí stávající substring novým substringem a to pro zadaný počet substringů (implicitně pro všechny).

>>> ring = "horo, horo, vysoká jsi"
>>> (fing := ring.replace("horo", "Horo", 1))
'Horo, horo, vysoká jsi'
Použitím metody replace lze částečně kompenzovat neexistenci procedury "remove" pro řetězce:

>>> abr = "abrakadabra"
>>> abr.replace("a", "")
'brkdbr'
V případě potřeby si můžeme napsat proceduru (zde funkci) sami, například chceme-li zbavit řetězec předdefinované sady znaků, prezentované jako "punctuation".
K vlastnímu vyzkoušení použijte prostředí IDLE:

import string

def remove_punct(s):
    s_without_punct = ""     proměnná zvaná akumulátor
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

str = "Až na severní pól, běží liška!"

print(remove_punct(str))

# Ctrl-S, F5
Až na severní pól běží liška
Poznámka:
>>> import string as str
>>> str.punctuation
"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
Cvičení: Můžeme si definovat vlastní soubor znaků, napříkad "žšěíó".
Pro jeho použití upravte funkci remove_punct(s).
Metoda 'find'
Vrací index prvního výskytu zadaného substringu v prohledávaném řetězci. Schéma volání metody find (parametry v hranatých závorkách jsou nepovinné) je toto:

string.find(sub [,start [, end]])

sub - hledaný substring
start - začátek hledání; implicitně je 0
end   - konec hledání; implicitně konec řetězce
Metoda find je ve skutečnosti všestrannější než naše uživatelská funkce. Umí nalézt i části řetězců, nejenom pouhé znaky:

>>> tanec = "Dokolečka dokola"
>>> tanec.find("leč")
4
Jako naše funkce i tato metoda přijímá nepovinný argument, který určuje index u kterého má začít:

>>> tanec.find("kol", 4)
12
Odlišně od naší funkce, druhý nepovinný parametr metody určuje index, kde má hledání skončit:

>>> tanec.find("la", 1, 15)
-1                        # návratová hodnota v případě neúspěchu
V tomto případě skončí hledání nezdarem, protože se substring la nevyskytuje v intervalu od 1 do 15 (nikoliv včetně).

Metoda 'count'
Vestavěnou metodu count použijeme při počítání výskytu zadaného znaku či skupiny znaků v řetězci:

string.count(value [, start [, end]])
>>> "abrakadabra".count("a")
5
>>> "abrakadabra".count("ra")
2
>>> "Až na severní pól".count(" ")
3

6.13 Sestavení funkce 'find'
Uživatelská funkce find přijme znak a nalezne index místa, kde se znak nachází. Není-li znak nalezen, funkce vrací -1.

def find(strng, ch):
    index = 0
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
V této funkci se opět setkáváme s příkazem return uvnitř smyčky. Je-li str[index] == ch, je funkce ukončena předčasným přerušením smyčky.

Není-li znak v řetězci obsažen, potom program opustí smyčku normálně a vrátí -1.

Tento způsob výpočtu je někdy nazýván traverzování Heuréka, protože jakmile nalezneme co hledáme, můžeme zvolat „Heuréka” a skončit hledání.

Pro stanovení počátku pro hledání můžeme do funkce přidat třetí parametr:

def find1(strng, ch, start):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
Volání find1("banana","a",2) nyní vrátí pozici prvního a za indexem 2.
Funkci si vylepšíme úpravou parametru start. Připojením hodnoty z něj učiníme paramter s počáteční hodnotu, který je volitelný v tom smyslu, že jej můžeme při volání případně vynechat:

def find2(strng, ch, start=0):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
Výsledek volání find2("banana", "a", 2) bude stejný jako find1("banana", "a", 2), zatímco při volání find2("banana", "a") bude parametr start nastaven na počáteční hodnotu 0.
Přidáním dalšího volitelného parametru do fce find zajistíme prohledávání jak dopředu, tak dozadu:

def find3(strng, ch, start=0, step=1):
    index = start
    while 0 <= index < len(strng):
        if strng[index] == ch:
            return index
        index += step
    return -1
Zadání hodnoty -1 pro step způsobí zmenšování stavu počítadla. Pro tuto změnu bylo nutné ošetřit jak horní tak i dolní mez proměnné index.

6.14 Formátování řetězců I
Starší a v Pythonu 3.x stále použitelný způsob formátování řetězce je s použitím interpolačního operátoru % spolu s konverzními specifikacemi.

Konverzními specifikacemi jsou znaky, které zastupují zamýšlený formát vkládané hodnoty, například:

%d dekadické číslo celé
%f desetinné číslo
%s řetězec - lze vynechat
Schema formátování řetězce vypadá takto:

<FORMAT >  %  < ( VALUES ) >
Část FORMAT obsahuje kombinaci řetězců a konverzních specifikací. Následuje samotný interpolační operátor % a za ním výčet hodnot, doplňovaných za konverzní specifikace. Závorky jsou nepovinné, je-li hodnota pouze jedna.
Nejlépe si to ukážeme na několika příkladech:

>>> "Jmenuje se %s." % "Arthur"
'Jmenuje se Arthur.'
>>> name = "Alice"
>>> age = 10
>>> "I am %s and I am %d years old." % (name, age)
'I am Alice and I am 10 years old.'
>>> n1 = 4
>>> n2 = 5
>>> "2**10 = %d and %d*%d = %f"  %  (2**10, n1, n2, n1*n2)
'2**10 = 1024 and 4*5 = 20.000000'
>>>
V prvním uvedeném příkladě je jediná konverzní specifikace %s, která označuje řetězec. K ní se přiřazuje jediná hodnota "Arthur" a není uzavřena v závorkách.

Ve druhém příkladě má name hodnotu řetězce "Alice" a age má hodnotu celého čísla 10. Tyto se přiřazují ke dvěma konverzním specifikacím %s a %d; druhá specifikace je označením celého dekadického čísla.

Ve třetím příkladě mají proměnné n1 a n2 celočíselné hodnoty 4 a 5. Ve formátovaném řetězci jsou čtyři konverzní specifikace: tři %d a jedna %f. Písmeno f naznačuje, že příslušná hodnota má být ve tvaru čísla s plovoucí desetinnou čárkou. Čtyři hodnoty, které se vztahují k uvedeným čtyřem konverzním specifikacím jsou: 2**10,n1,n2 a n1*n2.

V následující ukázce vidíme povel k tisku bez formátování řetězce:

i = 1
print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
while i <= 10:
   print(i,'\t',i**2,'\t',i**3,'\t',i**5,'\t',i**10,'\t',i**20)
   i += 1
Tento program vytiskne tabulku různých mocnin čísel od 1 do 10. V uvedeném tvaru je rovnání výsledků do sloupců způsobené znakem tabelátoru (\t) které selhává jakmile hodnoty výsledků zaberou 8 míst:

i       i**2    i**3    i**5    i**10   i**20
1       1       1       1       1       1
2       4       8       32      1024    1048576
3       9       27      243     59049   3486784401
4       16      64      1024    1048576         1099511627776
5       25      125     3125    9765625         95367431640625
6       36      216     7776    60466176        3656158440062976
7       49      343     16807   282475249       79792266297612001
8       64      512     32768   1073741824      1152921504606846976
9       81      729     59049   3486784401      12157665459056928801
10      100     1000    100000  10000000000     100000000000000000000
Mohli bychom změnit šířku sloupce ale vidíme, že první sloupce již teď mají více místa než potřebují. Nejlepší bude určit šířku pro každý sloupec jednotlivě. Jak lze tušit, řešení poskytuje formátovaný řetězec :

i = 1
print("%-4s%-5s%-6s%-8s%-13s%-15s" %
   ('i', 'i**2', 'i**3', 'i**5', 'i**10', 'i**20'))
while i <= 10:
   print("%-4d%-5d%-6d%-8d%-13d%-15d" % (i, i**2, i**3, i**5, i**10, i**20))
   i += 1
Běh této verze dává následující výstup:

i   i**2 i**3  i**5    i**10        i**20
1   1    1     1       1            1
2   4    8     32      1024         1048576
3   9    27    243     59049        3486784401
4   16   64    1024    1048576      1099511627776
5   25   125   3125    9765625      95367431640625
6   36   216   7776    60466176     3656158440062976
7   49   343   16807   282475249    79792266297612001
8   64   512   32768   1073741824   1152921504606846976
9   81   729   59049   3486784401   12157665459056928801
10  100  1000  100000  10000000000  100000000000000000000
Pomlčka - za každou konverzní specifikací určuje zarovnání zleva. Číselné hodnoty určují minimální délku, takže %-13d je minimálně třináctimístné číslo zarovnané zleva.


6.15 Formátování řetězců II
Novější způsob formátování výstupu je pomocí metody .format() v sestavě "formátovaný_řetězec_s_výměnnými_poli" . format().

Výměnná pole jsou instrukce, uzavřené ve složených závorkách { }. Vše, co je mimo těchto závorek, je považováno za text, který je v nezměněném stavu kopírován do výstupu.

Pro popis skladby výměnného pole se domluvme, že hranatými závorkami označíme údaj, který může chybět.

Skladbu výměnného pole tedy vyjádříme schematicky takto:
{ [field_name] [!conversion] [:format_spec] }
Nejjednodušší možná forma výměnného pole jsou prázdné složené závorky { }.

Sektor  field_name
je buď číslo, nebo klíčové slovo. Číslo odkazuje na poziční argument, klíčové slovo na pojmenovaný argument metody .format(). Tvoří-li čísla řadu 0, 1, 2, ..., lze je vynechat.

Více než slova řekne ukázka:

>>> "Od {} do {}" .format("rána", 22.00)
'Od rána do 22.0'  # totéž jako "Od {0} do {1}"
>>> "Jmenuji se {name}" .format(name = "Pavel")
'Jmenuji se Pavel'
Sektor  !conversion
způsobí změnu typu před formátováním. Používá se značení
!s, které volá funkci str(), jež vrací objekt coby řetězec
!r, které volá funkci repr(), jež vrací řetězec obsahující tisknutelnou prezentaci objektu
!a, které volá funkci ascii(), jež vrací řetězec, jehož non-ASCII znaky jsou nahrazeny escape sekvencí.

Ukázka přiblíží způsob použití:

>>> "Harold je chytrý {0!s}" .format("chlapeček")
'Harold je chytrý chlapeček'
>>> "Harold je chytrý {0!r}" .format("chlapeček")
"Harold je chytrý 'chlapeček'"
>>> "Harold je chytrý {0!a}" .format("chlapeček")
"Harold je chytrý 'chlape\\u010dek'"        # ošetřené ne-ASCII
Sektor  :format_spec
upřesňuje, jak má být hodnota prezentována, to jest určuje:
šířku - pole pro zadávanou hodnotu
výplň - libovolný znak kromě závorek { }; následuje pokyn pro zarovnání
zarovnání - vlevo (<), vpravo (>), na střed (^) a mezi(=) signum a číslici
signum - +, -, " ", (také # a 0)
přesnost - počet desetinných míst čísla: . údaj
typ - určuje způsob prezentace dat, například b je pro binární formát, d je pro decimální celé číslo, f pro formát float

Ukázka přiblíží způsob použití:

>>> "{:<25}" .format("zarovnáno vlevo")
'zarovnáno vlevo          '
>>> "{:>25}" .format("zarovnáno vpravo")
'         zarovnáno vpravo'
>>> "{:ˇ^25}" .format("hulín")
'ˇˇˇˇˇˇˇˇˇˇhulínˇˇˇˇˇˇˇˇˇˇ'
Další zajímavé příklady namátkou:

>>> import math
>>> print("Hodnota Pí je asi {0:.3f}" .format(math.pi))
Hodnota Pí je asi 3.142
>>>
>>> telef = {"Jan":4127, "Dana":4098, "Ota":863678}
>>> for name, phone in telef.items():
        print("{0:10} ==> {1:10d}" .format(name, phone))
...
Ota        ==>    863678
Dana       ==>      4098
Jan        ==>      4127
Další příklady lze nalézt v literatuře (pohříchu anglické), například The Python Tutorial - Input and Output

Najde se tam také tento užitečný:

>>> for x in range(7,11):
...     print("{0:2d} {1:3d} {2:4d}" .format(x, x*x, x*x*x))
...
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>>

6.16 Formátování řetězců III
Nejnovější způsob formátování řetězců byl zaveden ve verzi Python 3.6. Označuje se jako formátovaný literál řetězce (formatted string literal), stručně f-string. Literál f-stringu se uvozuje písmenem f nebo F a lze použít obdobné konverze (!s, !r, !a) jako u předchozího způsobu.

Obdobně jako u předchozího způsobu může tento literál obsahovat výměnná pole, ohraničená složenými závorkami { }. Zatímco u předchozího způsobu odkazoval obsah těchto závorek pouze na konstantní hodnotu, u f-stringu může odkazovat také na výraz, funkci, metodu aj.

V následující ukázce vidíme volání funkce a metody:

>>> name = "IDLE"
>>> def to_lowercase(input):
...     return input.lower()

>>> f"{to_lowercase(name)} je zábavné."         volání funkce
'idle je zábavné.'

>>> f"{name.lower()} je zábavné."               volání metody
'idle je zábavné.'
V další ukázce je odkaz na slovník:

>>> postava = {'name': 'Petr Parléř', 'age': 67}
>>> f"Stavitel {postava['name']} se dožil " \
... f"{postava['age']} let."
'Stavitel Petr Parléř se dožil 67 let.'
# konverzní flag !a pro ASCII - viz 6.16:
>>> f"Stavitel{postava['name']!a}"
"Stavitel'Petr Parl\\xe9\\u0159'"
Ukázka interakce f-stringu s instancí třídy - viz Kapitola 12.9 a cvičení 12.15/6.

Python 3.8 přináší rozšíření f-stringu o rovnítko za jménem, které způsobí vytištění předem přiřazené hodnoty:

>>> python = 3.8

>>> f"{python=}"
'python=3.8'
>>> f"{python = :> 5}"            # případně s formátováním výstupu:
'python =   3.8'
Další možností je použití mrožího operátoru uvnitř f-stringu:

>>> import math
>>> r = 2.4
>>> f"Tyč o průměru {(d := 2 * r)} cm má obvod {math.pi * d:.2f} cm"
'Tyč o průměru 4.8 cm má obvod 15.08 cm'

6.17 Dokumentační řetězce
Kromě jednoduchých a dvojitých uvozovek zná Python také řetězce s trojitými uvozovkami, tvořenými jednoduchými i dvojitými znaky. Řetězce mohou procházet přes více řádků.

>>> """Toto je jedna možnost."""

>>> '''Toto je druhá možnost.'''
Uvnitř řetězce s trojitými uvozovkami mohou být uvozovky jednoduché i dvojité:

>>> ''' "Ach ne", zvolala, "Benovo kolo je rozbité" '''
' "Ach ne", zvolala, "Benovo kolo je rozbité" '
>>>
Trojité uvozovky se používají pro dokumentační řetězce (docstrings). Docstring je řetězec, umístěný jako první text v modulu, funkci, třídě nebo v definici metody:

def mocnina(m, n=3):
    '''
    Funkce počítá n-tou mocninu s pevně
    nastaveným exponentem n=3; lze jej změnit
    '''
    print(m**n)
Informaci o funkci získáme evokací (voláním, neboli také "aplikací") vestavěné metody .__doc__ pro objekt funkce:

>>> print(mocnina.__doc__)
Funkce počítá n-tou mocninu s pevně
nastaveným exponentem n=3; lze jej změnit
>>>
Dokumentačního řetězce použijeme k získání stručné informace o jakémkoli vestavěném objektu (funkci):

>>> print(len.__doc__)
Return the number of items in a container.
>>>

6.18 Glosář
sekvence (sequence)
Uspořádaná množina prvků. Podmnožina této množiny se nazývá subsekvence.
index
Interní hodnota, použitá k označení prvku uspořádané řady, na příklad znaku v řetězci.
traverzovat (traverse)
Probírat postupně jednotlivé prvky dané řady a s každým provést obdobnou operaci.
úsek (slice)
Část řetězce, vymezená rozsahem indexů.
whitespace
Netištěné znaky pro ovládání kurzoru. Všechny tyto znaky obsahuje konstanta string.whitespace.
dokumentační řetězec (docstring)
Řetězcová konstanta, uvedená na prvním řádku funkce nebo modulu (a jak uvidíme později i třídy a metody). Dokumentační řetězce vhodně spojují programový kód s jeho komentářem. Používají se také pro automatické testování kódu s modulem doctest.
6.19 Cvičení
V návaznosti na odstavec 6.7 upravte skript tak, aby se Ouack a Quack vytiskly správně:
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)
Zapouzdřete následující sekvenci příkazů do funkce count_letters_acc
fruit = "banana"
count = 0
for char in fruit:
    if char == 'a':
        count = count + 1
print(count)
a zobecněte ji tak, aby přijímala řetězec a písmeno jako argument a vracela počet výskytů písmena v řetězci. Řešení vložte do skriptu whatLetters_str.py
Tutéž úlohu (výskyt znaků) řešte vestavěnou metodou string.count(letters), která počítá výskyt nejenom písmen ale i zadaných substringů.
V následujících úlohách použijeme k ověření správnosti vašeho řešení doctesty, se kterým jsme se seznámili v kapitole 5.10. Vytvořte soubor se jménem stringtools.py a na jeho spodní okraj vložte tento veršíček:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
Přidávejte těla funkcí tak, aby prošla zkouškou doctestů. Ty budou u některých výsledků vyžadovat i apostrofy. Přičtete je k výstupu:
print("'" + <výstup> + "'")
nebo použijte funkci
return <výstup>
Návštěva stránky String Methods může být v případě potřeby prospěšná.

def reverse (s):
   """
   >>> reverse('happy')
   'yppah'
   >>> reverse('Python')
   'nohtyP'
   >>> reverse('')
   ''
   >>> reverse('P')
   'P'
   """
Jednoduché řešení úsekovým operátorem

def mirror (s):
    """
    >>> mirror ('good')
    'gooddoog'
    >>> mirror ('yes')
    'yessey'
    >>> mirror ('Python')
    'PythonnohtyP'
    >>> mirror ('')
    ''
    >>> mirror ('a')
    'aa'
    """
Prosté spojení dvou řetězců.

def is_palindrome (s):
    """
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abab')
    False
    >>> is_palindrome('tenet')
    True
    >>> is_palindrome('banana')
    False
    >>> is_palindrome('straw warts')
    True
    """
Použijete řešení ad a).

def remove_letter (letter, strng):
    """
    >>> remove_letter ('a', 'apple')
    'pple'
    >>> remove_letter ('a', 'banana')
    'bnn'
    >>> remove_letter ('z', 'banana')
    'banana'
    >>> remove_letter ('i', 'Mississippi')
    'Msssspp'
    """
Lze řešit prostřednictvím idiomu for .. in .. nebo metodou replace.

def count_sub (sub, s):
    """
    >>> count('is', 'Mississippi')
    2
    >>> count('an', 'banana')
    2
    >>> count('ana', 'banana')
    1
    >>> count('nana', 'banana')
    1
    >>> count('nanan', 'banana')
    0
    """
Napoví stránka "String Methods".

def remove_sub (sub, s):
    """
    >>> remove('an', 'banana')
    'bana'
    >>> remove('cyc', 'bicycle')
    'bile'
    >>> remove('iss', 'Mississippi')
    'Missippi'
    >>> remove('egg', 'bicycle')
    'bicycle'
    """
Napoví stránka "String Methods".

def remove_all (sub, s):
    """
    >>> remove_all('an', 'banana')
    'ba'
    >>> remove_all('cyc', 'bicycle')
    'bile'
    >>> remove_all('iss', 'Mississippi')
    'Mippi'
    >>> remove_all('egg', 'bicycle')
    'bicycle'
    """
Vyzkoušejte následující formátující řetězcové operace v konzole Pythonu a zaznamenejte výsledky:
>>> "%s %d %f" % (5,5,5)

>>> "%-.2f" % 3

>>> "%-10.2f %-10.2f" % (7, 1.0/2)

>>> print(" $%6.2f\n $%6.2f\n $%6.2f" % (3, 4.5, 11.2))

Totéž proveďte pomocí funkce .format().
previous    up  next    hi  end endswith

# ================================
miko oddel
# ================================
7.1 Soubory
# ================================

Textový soubor je počítačový soubor (stream), složený ze znaků tisknutelných - které slouží k vyjádření obsahu a netisknutelných (řídících) - které slouží pro označení mezer, tabulátorů, konce řádku aj.

Cokoli máme v počítači uloženo v paměti na disku, je uloženo v binárním formátu. Při otevírání souboru v nějaké aplikaci (například v textovém editoru či v Průzkumníku souborů) je binární formát automaticky převeden do formátu, který lze číst nebo prohlížet. V prostředí Pythonu nám práci s binárním formátem umožňuje existence datového typu bytes.

Při práci s textovým i binárním souborem musíme znát dvě věci - kde je soubor uložen a v jakém kódování (UTF-8, ASCII, ...) byl textový soubor uložen, neboli převeden do binárního formátu.
Před vlastní manipulací s obsahem souboru musíme soubor otevřít funkcí open(~), po ukončení úprav musíme soubor zavřít funkcí close().


7.2 Datový typ bytes, bytearray
Entita typu bytes (bytearray) je neměnná (měnitelná) sekvence bitů. Tato binární serializace je nutná pro uložení dat do paměti počítače nebo pro jejich transport po síti.
Mnohá data (obrázky, zvuk, text) lze serializovat (kódovat - encode) na bytes či deserializovat (dekódovat - decode) z bytes s použitím vhodného protokolu, jako je PNG, WAW, JSON nebo UTF-8, ASCII, cp1250 aj.
Prezentaci objektu ve formátu bytes, bytearray lze provést dvojím způsobem a to literálovou formou nebo s použitím příslušných funkcí či metod.

Literálový zápis objektu typu 'bytes' vytvoříme předznamenáním literálu řetězce písmenem b:

>>> asci = "Za horami, za lesy"           # kódování ASCII
>>> utf8 = "Až na severní pól"            # kódování UTF-8

Literálová forma:
>>> lba = b'Za horami, za lesy'; lba
b'Za horami, za lesy'
>>> lbu = b'Až na severní pól'; lbu       # pro řetězce nelze použít
SyntaxError: bytes can only contain ASCII characters.
>>> lb = b'(1, 2, 237)'; lb
b'(1, 2, 237)'
>>>lbn = b'range(12)'; lbn, type(lbn)
(b'range(12)' <class 'bytes'>)
Co k tomu dodat? Serializaci stringu literálovou formou lze provést jen tehdy když se formátovaný řetězec skládá pouze ze znaků, obsažených v kódování ASCII.

Převod řetězce na bytes pomocí funkce a metody
Převod na bytes lze provést pro všechny myslitelné znaky, ovšem patřičně ošetřené s použitím takzvané escape sekvence. Tu za nás při tvorbě objektu provede funkce bytes či bytearray, přijímající tři nepovinné parametry:

bytes([source[, encoding[, errors]]])
source - zdrojem může být řetězec, list, tuple, set, dict, integer, range; není-li uveden zdroj, vytvoří se prázdný objekt
encoding - povinné při kódování řetězce, např 'utf-8'
errors - uvedení akce, která se provede, když selže konverze řetězce, např. errors='strict'.
>>> bytes(asci, "utf-8")                    # kódování je povinné
b'Za horami, za lesy'
>>> bytes(utf8, "utf-8")
b'A\xc5\xbe na severn\xc3\xad p\xc3\xb3l'   # kombinace s 'escape sekvencí'
Znaky které patří do ASCII, jsou uvedeny normálně, znaky, které nejsou součástí ASCII, jsou vyjádřeny hexadecimálními čísly za zpětnými lomítky (což je ta escape sekvence). Na příkladě také vidíme, že znaky ž, í, ó jsou v UTF-8 vyjádřeny dvěma kódovými čísly.

Vedle funkce bytes(~) existuje také metoda encode(string, "coding"). Údaj o kódování lze vypustit, pokud souhlasíme s implicitně nastaveným utf-8. Pokud chceme použít jiné kódování, musíme jej uvést:

>>> "píšež".encode()                      # kódování utf-8 implicitně
b'p\xc3\xad\xc5\xa1e\xc5\xbe'
>>> "píšež".encode('utf-16')
b'\xff\xfep\x00\xed\x00a\x01e\x00~\x01'   # jsme poněkud někde jinde
Převod bytes na řetězce
Při deserializaci (decoding) objektu typu bytes na řetězec musíme vědět, jaké kódování bylo při serializaci použito. To není vždy spolehlivě zjistitelné. Jeden způsob je popsán zde.
Pro převod použijeme metodu bytes.decode("coding"):
>>> bczstr = bytes("píšež", "utf-8")       # objekt typu bytes
>>> bczstr.decode("utf-8")                 # kódování je povinné
'píšež'
Lze také použít funkci str(bytes-obj, 'coding'):

>>> str(bczstr, "utf-8")                   # kódování je povinné
'píšež'
Bytearray
Jediná odlišnost typu bytearray od typu bytes spočívá v tom, že bytearray podporuje měnitelnost.

>>> bs = bytes('souznění', 'utf-8'); bs        # objekt typu bytes
b'souzn\xc4\x9bn\xc3\xad'                      # nejde změnit
>>> ba = bytearray('souznění', 'utf-8'); ba
bytearray(b'souzn\xc4\x9bn\xc3\xad')           # objekt typu bytearray
>>> ba[0] = 108                                # ord("l") = 108
>>> aba = bytearray("b", "utf-8") + ba; aba
bytearray(b'blouzn\xc4\x9bn\xc3\xad')
>>> str(aba, "utf-8")                          # převod na řetězec
'blouznění'
Jak vidno, objekt typu bytearray je vlastně objekt typu bytes, dekorovaný slovem bytearray.


7.3 Práce s textovými soubory
Otevření souboru funkcí open(~) vytváří souborový objekt (file_object), označovaný také jako stream:

file_object = open('file_name' [, 'access_mode'] [, coding] [, buffering])
                        # hranaté závorky označují nepovinný argument
file_name   název souboru včetně přípony
access_mode přístupový režim pro manipulaci se souborem
coding      žádané kódování např. coding="utf-8" či "cp1250" (nebo "ASCII")
buffering   nastavení velikosti vyrovnávací paměti - nebudeme používat

Přístupové režimy
Přístupový režim (mód) určuje, jakou manipulaci lze s otevřeným souborem provádět. Není-li režim zadán, je implicitně nastaven režim read. Zároveň určuje polohu interního 'ukazovátka', označujícího počáteční místo pro případnou manipulaci.

'r' (read)  pouze pro čtení; ukazovátko na začátku souboru
'w' (write) pouze pro psaní; ukazovátko na začátku souboru; přepisuje existující soubor, neexistující vytvoří
'a'  (append) pro připojení textu; ukazovátko na konci existujícího souboru; neexistující soubor vytvoří
'rb', 'wb', 'ab'  totéž co 'r', 'w', 'a' ale pro binární soubor
'r+', 'rb+' pro čtení i psaní - pozor, přepisuje existující soubor
Těmto režimům je lépe se vyhnout:
'w+', 'wb+' pro psaní i čtení; přepisuje existující soubor, neexistující vytvoří
'a+', 'ab+' pro připojení textu i čtení; neexistující soubor vytvoří
Manipulaci se souborovým objektem (streamem) si ukážeme na několika příkladech.

>>> myfile = open('test.dat', 'w')       # zde vytváříme nový soubor
>>> print(myfile)
<_io.TextIOWrapper name='test.dat' mode='w' encoding='cp1250'>
Příkaz print nám vrátil typ objektu, jméno souboru, použitý mód a kódování souboru.

Neexistuje-li soubor se jménem test.dat, bude vytvořen v aktuálním adresáři. Jestliže takový soubor v režimu "w" již existuje, bude jeho text nahrazen textem, který případně zapíšeme.

Pro vkládání dat do souboru použijeme metodu souborového objektu write. Pokud proceduru 'write' provádíme v jedné seanci opakovaně, k přepisu stávajícího textu nedojde. K přepisu dojde u nově aktivovaného souborového objektu.

>>> myfile.write("Nyní je čas")                    --> 11 znaků
>>> myfile.write(" zavřít soubor.")                --> 15 znaků
Zavření souboru říká systému, že jsme skončili zapisování a soubor je možné zavřít:

>>> myfile.close()
Nyní můžeme soubor opět otevřít, tentokrát pro čtení a načíst jeho obsah do řetězce v našem programu.

>>> myfile = open('test.dat', 'r')
Pokusíme-li se otevřít soubor, který neexistuje, dostaneme chybové hlášení:

>>> myfile = open('test.cat', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'test.cat'
Pokusíme-li se otevřít soubor s českým textem, dostaneme toto chybové hlášení:

>>> fruten = open("cz_fruits.txt")
>>> next(fruten)
...
UnicodeDecodeError: 'charmap' codec can't decode
byte 0x88 in position 27: character maps to <undefined>
... kodek 'charmap' neumí dekódovat bajt 0x88 (136) na pozici 27
Náprava spočívá v tom, že zadáme rovněž parametr 'coding':

>>> fruten = open("cz_fruits.txt", encoding="utf-8")
>>> next(fruten)

Metoda read bez argumentů načte celý obsah do jediného řetězce:

>>> print(myfile.read())
Nyní je čas zavřít soubor.
>>> myfile.close()
Metoda read může také přijmout argument, který říká kolik znaků má být čteno:

>>> myfile = open('test.dat')       # nutno znovu "naládovat"
>>> print(myfile.read(7))
Nyní je
Zadáme-li číslo větší než je počet znaků v souboru, vrátí read jen zbývající znaky. Došlo-li se na konec souboru, vrátí read prázdný řetězec:

>>> print(myfile.read(726))
 čas zavřít soubor.
>>> print(myfile.read())
                                    # nemáme "naládováno"
>>>
Podivné chování metody read() je důsledkem toho, že souborový objekt je také iterátorem a když opět nahlédneme do kap. 4.6, tak si připomeneme, že iterátorový objekt vlastní funkci next(), která posouvá interní index objektu a jejíž použití si nyní opět ukážeme.
Otevřeme si soubor unsorted_fruits.txt a jeho obsah vložíme do souboru "fruits.txt", který vložíme do složky, v níž následně aktivujeme konzolu interpreta Pythonu. Ze souboru vytvoříme souborový objekt (neboli iterátor):

>>> fru = open("fruits.txt")
>>> next(fru)
'papaya\n'                 # \n označuje konec řádku
>>> next(fru)
'kiwifruit\n'
...
>>> next(fru)
StopIteration              # vyčerpali jsme celý seznam
>>> fru.read()
''                         # potvrzeno, vrabci vyklobali
Potřebujeme-li z objektu znovu číst, musíme přesunout jeho ukazovátko (pointer) na začátek - a to nejlépe metodou seek(offset[, from]):

>>> fru.seek(0, 0)          # jsme opět na začátku!
>>> print(fru.readline())   # vrátí obsah aktuálního řádku
papaya
>>> print(fru.readlines())  # vrátí seznam řetězců, obsahujících zbývající řádky
papaya
>>> print(fru.tell())       # sdělí pozici ukazovátka
8
>>> fru.close()             # zavřít objekt se vřele doporučuje
Metoda readline() přečte všechny znaky z prvního řádku včetně znaku newline:

Metoda readlines() vrátí všechny zbyvající řádky jako seznam řetězců:

Automatické zavření objektu nám zajistí použití idiomu with :

with open("week.txt", "w") as dny:
   dny.write("pondělí\núterý\nstředa\nčtvrtek\npátek\nsobota\nneděle\n")

Soubor je zavřen, pro novou manipulaci jej musíme opět otevřít

with open("week.txt") as ven:
   for line in ven.readlines():
      print(line, end='')
Skript vytvořil v aktuálním adresáři soubor 'week.txt' (pokud již neexistoval) a vložil do něho dny týdnu. Při dalším otevření souboru (implicitně v režimu 'read') jsme předepsali jejich postupný výtisk v konzole. Po ukončení práce se soubor sám zavřel.
Ověřte si to v aplikaci IDLE Pythonu.

Následující funkce kopíruje soubor tak, že přečte a zapíše nejvíce 50 znaků najednou. První argument je jméno původního souboru, druhý argument je jméno nového souboru:

Soubor copy_file.py

def copy_file(oldfile, newfile):       # názvy souborů v uvozovkách
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
    while True:
        text = infile.read(50)
        if text == "":
            break
        outfile.write(text)
    infile.close()
    outfile.close()
    return
Tato funkce cyklicky čte 50 znaků z infile a zapisuje je do outfile až je dosaženo konce a text je prázdný řetězec, čímž se vyvolá provedení příkazu break.
Soubor copy_file.py uložte do složky, kde máte soubor oldfile. Používáte IDLE Pythonu.


7.4 Práce s binárními soubory
Soubory, které obsahují fotografie, obrázky, videa, zvukový záznam, zipové a spustitelné soubory - se nazývají binární soubory. Tyto soubory nejsou organizovány do řádků a nelze je (užitečně) otevřít normálním textovým editorem.

V Pythonu tyto soubory regulerně otevřeme již popsanou funkcí open v režimu rb (read binary) a wb (write binary). V následující ukázce vytvoříme binární kopii velikonočního pozdravu:

# copy-easter.py

f = open("easter_328kb.jpg", "rb")   # existující kopírovaný soubor
g = open("easter_copy.jpg", "wb")    # nový (prázdný) soubor tamtéž

while True:
    buff = f.read(3300)              # pomocný objekt 3300 bitů
    if len(buff) == 0:
         break
    g.write(buff)

f.close(); g.close()
Soubor easter_328kb.jpg si prohlédnete zde , otevřený obrázek si v otevřeném kontextovém menu uložíte volbou "Save image as...". Pro potěšení si posléze ve svém adresáři otevřete také easter_copy.jpg

V následující ukázce si vytvoříme nový soubor a vložíme do něho text v kódování utf-8. Následně si tento soubor otevřeme jako objekt typu bytes:

# with-open.py

with open("cat.txt", "w", encoding="utf-8") as catt:
    catt.write("Kočička")

with open("cat.txt", "rb") as catt:
    data = catt.read()
>>> data
b'Ko\xc4\x8di\xc4\x8dka'
>>>
Ve výstupu vidíme, že písmeno "č" se v utf-8 vyjádří pomocí dvou bajtů, což se v zápisu binárního řetězce (který je implicitně kódován v ASCII) projeví aplikací "escape sekvence".


7.5 Adresáře
Soubory uložené na trvalých paměťových nosičích jsou uspořádány podle souboru pravidel, známého jako souborový systém (file system). Tento systém se skládá ze souborů a složek (folders) neboli adresářů (directories), což jsou kontejnery jak pro soubory, tak pro další složky.

Nově vytvořený soubor se po otevření a zápisu uloží do aktuálního adresáře (to jest do toho, ve kterém se nalézáme při provádění programu). Nebo naopak, otevíráme-li soubor pro čtení, hledá jej Python v aktuálním adresáři.

Chceme-li otevřít soubor někde jinde, musíme k němu určit cestu, například:

>>> wordsfile = open('/usr/share/dict/words.txt', 'r')
>>> wordlist = wordsfile.readlines()
>>> print(wordlist[:5])
['\n', 'A\n', "A's\n", 'AOL\n', "AOL's\n", 'Aachen\n']
Tento příklad otevírá soubor se jménem words.txt, který je uložený v adresáři se jménem dict jenž se nalézá v adresáři share, kterýžto je uložen v adresáři usr, jenžto sídlí v nejvyšším systémovém adresáři, označeném /. Program potom načítá jednotlivé řádky do seznamu se jménem wordlist s použitím metody readlines a posléze vytiskne prvních pět položek vytvořeného seznamu.

Znak / nelze použít jako součást jména souboru; je vyhrazen jako vymezovač mezi jmény adresářů a souborů.

Soubor /usr/share/dict/words.~ by měl existovat na unixových systémech a obsahovat abecedně uspořádaný seznam slov.


7.6 Vytváření a import modulů
Velké množství užitečných příkazů a funkcí je uloženo v takzvaných modulech, což jsou prosté soubory s příponou .py. Vestavěné (built-in) moduly jsou psány v jazyce C a jsou součástí interpreta Pythonu.

Příkladem vestavěných modulů jsou moduly math, string, random, sys ,   se kterými se postupně seznámíme.

K vytvoření vlastního modulu nám stačí textový soubor s příponou .py. Název souboru nesmí být rozdělen pomlčkou, přípustné je podtržítko.

# Text souboru mojevoje.py

def mocnina(m, n=3):            # Jen deklarace funkce
    print(m**n)

print("Quo vadis?")             # Přímo proveditelný příkaz

def print_twice(spam):          # Jen deklarace funkce
    print(spam, spam)
Tento skript můžeme realizovat přímo, voláním ze systémové konzoly (nebo přes F5 v IDLE):

F:\Codetest\HowTo\ch-07> python mojevoje.py
Quo vadis?
Ve spuštěném souboru se ihned provede přímo proveditelný text. Bohužel, k této aktivitě dochází i při importu modulu.

Máme-li soubor:

# tvojevoje.py
import mojevoje
můžeme jej aktivovat z konzoly:

F:\Codetest\HowTo\ch-07> python tvojevoje.py
Quo vadis?             # výstup realizovaného textu z importu

Import modulu lze provést trojím způsobem (konzolu Pythonu otevřeme ve složce, která obsahuje soubory mojevoje.py a tvojevoje.py):

a)

F:\Codetest\HowTo\ch-07> python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, ...
Type "help", "copyright", "credits" or ...
>>>
>>> from mojevoje import mocnina
Quo vadis?
>>> mocnina(5)
125
b)

>>> from mojevoje import *            # importuje se vše z modulu
Quo vadis?
>>> mocnina(5, 2)
25
>>> print_twice("hola ")
hola hola
c)

>>> import mojevoje
Quo vadis?
>>> mojevoje.mocnina(4)               # evokace tečkovou notací
64
V prvním příkladě má být importována pouze funkce mocnina ale jak vidíme, importuje se rovněž realizovatelný text modulu.

V druhém případě jsme importovali vše z označeného modulu. Tento způsob nebývá doporučován, protože může vést ke kolizi jmen.

Ve třetím příkladě jsme importovali celý objekt modulu a pro použití některého jeho atributu (zde funkce) musíme uplatnit tečkovou notaci, to jest sekvenci:

<název modulu>.<název atributu>
Samostatně proveditelný příkaz print("Quo vadis?") se opět provedl bez našeho přičinění, což je vlastně svého druhu problém.
Eliminovat jej lze tím, že ze souborů, kde se "povalují" samostatně proveditelné příkazy, nebudeme nic importovat nebo tyto příkazy umístíme za karanténní bariéru:

# Text souboru mojevoje_alt.py

def mocnina(m, n=3):               # Jen deklarace funkce
    print(m**n)

if __name__ == "__main__":         # idiom Pythonu
    print("Quo vadis?")            # Přímo proveditelný příkaz

Připojení cesty k modulu
Importujeme-li modul, musíme mít k němu zajištěnou cestu tím, že:

se modulový soubor nachází ve stejném adresáři jako zdrojový soubor - tento způsob jsme dosud předpokládali
v záhlaví zdrojového souboru uvedeme cestu k modulovému souboru (například 'mojeVoje.py') ve složce 'F/Codetest/Howto/ch-07/'. Je-li IDLE otevřen ve složce 'F/Codetest/Howto/', doplníme zbytek cesty:
>>> import sys
>>> sys.path.append("ch-07/")

>>> import mojevoje
Quo vadis?          # importovaný soubor se v možném rozsahu
                      ihned realizuje
máme-li soubor, který můžeme často používat jako modul, můžeme jej vložit do instalační složky Pythonu ../Lib/site-packages; umístění této složky zjistíme (z jiného místa) dotazem:
>>> import sys
>>> print(sys.path)
Takto uložený soubor můžeme importovat odkudkoli.
Poznámka
Stejného účinku dosáhneme, jestliže máme v Console2 nastaveno aby se konzola Python spouštěla v téže složce, kde odkládáme své modulové soubory.
Import modulu z paketu
Paket (package) je adresář, který obsahuje povinně soubor (třeba prázdný) __init__.py, spolu s potřebnými soubory (moduly) ~ .py.

Mějme například složku intext/ se soubory __init__.py a foo.py.

# Text souboru ch-07/intext/foo.py

class Foo:                  # deklarace třídy (viz kap. 12)
    def ukul(self):         # metoda (funkce) třídy
        print("Ukulele")
Ukulele si můžeme vytisknout v konzole, otevřené ve složce ch-07:

>>> import intext.foo           # deklarace cesty k modulu
>>> inst = intext.foo.Foo()     # vytvoření instance třídy
>>> inst.ukul()                 # volání metody třídy
Ukulele

7.7 Modul sys a proměnná argv
Modul sys obsahuje funkce a proměnné, které poskytují přístup k prostředí operačního systému, ve kterém běží překladač Pythonu. Následující příklad ukazuje výstupní hodnoty několika příkazů, zadaných na některém z našich počítačů:

>>> import sys
>>> sys.platform
'win32'

>>> sys.path
['', 'G:\\Python\\python36.zip', 'G:\\Python\\DLLs', 'G:\\Python\\lib', 'G:\\Python', 'G:\\Python\\lib
\\site-packages']

>>> sys.version
'3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]'
Úplný obsah modulu sys nám vrátí funkce:

>>> dir(sys)
Proměnná argv obsahuje seznam argumentů, načtených z příkazového řádku při spuštění skriptu. Prvním načteným argumentem (s indexem 0) je název souboru.

Vytvořme skript demo_argv.py

# f:/codetest/howto/ch-07/demo_argv.py

import sys

print(sys.argv[0])        # --> prázdný řádek
print(sys.argv)           # --> ['']
Spustíme jej z příkazového řádku zároveň s argumenty (viz) a obdržíme:

F:\Codetest\HowTo\ch-07 > python demo_argv.py this and that 1 2 3
demo_argv.py
['demo-argv.py', 'this', 'and', 'that', '1', '2', '3']
Argumenty, mezi něž patří i název skriptu, jsou odděleny pouze mezerou. Chceme-li zadat argumenty s uskupením, použijeme uvozovky:

F:\Codetest\HowTo\ch-07 > python demo_argv.py "this and that"  "1 2" 3
['demo_argv.py', 'this and that', '1 2', '3']
Pomocí argv můžeme psát užitečné programy, které přijímají vstupy přímo z příkazového řádku. Zde je například program, který určí součet zadané řady čísel:

# sum.py

from sys import argv

nums = argv[1:]           # index '0' je vyhrazen pro název souboru

# Funkce enumerate(~) vytváří z objektu 'nums' iterátor - viz 4.9.
for index, value in enumerate(nums):
    nums[index] = float(value)

print(sum(nums))
V tomto programu používáme způsob importu from <module> import <attribute>, při kterém je proměnná argv přenesena do jmenného prostoru modulu.

Nyní můžeme spouštět program z příkazové řádky takto:

>>> F:\Codetest\HowTo\ch-07 > python sum.py 3.5 5 11 100
119.5

7.8 Modul pydoc
Modul pydoc použijeme k prohledávání knihoven Pythonu, instalovaných na počítači. Na příkazový řádek napíšeme:

F:\HowTo> python -m pydoc -b
Server ready at http://localhost:52142/
Server commands: [b]rowser, [q]uit
server>
Příkaz spustí libovolný nepoužitý port v počítači a otevře stránku ve webovém počítači. Seanci ukončíme zavřením stránky a zápisem q za poslední port v konzole.


Je to výčet všech knihoven Pythonu na vašem počítači. Klikem na jméno modulu otevřeme novou stránku s dokumentací o vybraném modulu. Například, klik na slovu keyword otevře následující stánku:


Dokumentace pro většinu modulů obsahuje tři barevně označené sektory:

pro třídy - růžový
pro funkce - oranžový
pro data - zelený
Modul keyword obsahuje jedinou funkci iskeyword, která - jak její jméno naznačuje - je booleovskou funkcí, vracející True je-li zadaný řetězec klíčovým slovem:

>>> from keyword import *
>>> iskeyword('for')
True
>>> iskeyword('all')
False
>>>
Datový prvek kwlist obsahuje seznam všech současných klíčovych slov Pythonu:

>>> from keyword import *
>>> print(kwlist)
['and', 'as', 'assert', 'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from',
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
'False', 'None', 'True']
>>>
Doporučujeme časté používání služby pydoc ke zkoumání rozsáhlých knihoven Pythonu. Mnoho pokladů čeká na své objevení!


7.9 Glosář
modul (module)
Soubor obsahující definice a příkazy Pythonu určené pro použití v jiných pythonovských programech. Obsah modulu je zpřístupněn použitím příkazu import .
standardní knihovna (standard library)
Knihovna je kolekce programů, používaných jako nástroje při vytváření jiných programů. Knihovny jsou nedílnou součástí programovacích jazyků. Python má bohatou standardní knihovnu.
pydoc
Generátor dokumentace, který je součástí standardní knihovny Pythonu.
příkaz k importu (import statement)
Příkaz, který zpřístupní objekty ze zadaného souboru - např. mymod.py. Jsou tři formy tohoto příkazu:
import mymod
importuje celý modul mymod,
from mymod import *
importuje vše z modulu mymod,
from mymod import f1, v1
importuje z modulu mymod jen objekt f1 a v1.
jmenný prostor (namespace)
Syntaktický kontejner, který umožňuje aby totéž jméno mohlo být součástí různých jmenných prostor bez víceznačností. Jmenné prostory v Pythonu se tvoří pro moduly, třídy, funkce a metody.
jmenná kolize (naming collision)
Situace, při které nelze od sebe rozlišit dvě nebo více jmen v daném jmenném prostoru. Použítím
import string
# a posléze s použitím tečkové notace
string.method_name()
místo
from string import *
zabráníme jmenné kolizi.
atribut (attribute)
Proměnná či funkce, která je definovaná uvnitř modulu (nebo třídy či instance, jak uvidíme později). Atributy modulů jsou přistupné s použitím tečkového operátoru (.).
metoda (method)
Funkce, definovaná uvnitř třídy. Metody se pro objekt evokují s použitím tečkového operátoru, například:
>>> s = "this is a string"
>>> s.upper()
'THIS IS A STRING'
>>>
Říkáme, že metoda upper je volána pro řetězec s.

nestálá paměť (volatile memory)
Paměť, která k zachování stavu potřebuje stálý příkon elektrické energie. Hlavní paměť počítače, neboli RAM je nestálá. Informace, uložená v paměti RAM se ztratí při vypnutí počítače.
trvalá paměť (non-volatile memory)
Paměť, která svůj stav udržuje bez elektrické energie. Pevné disky, měnitelné disky a přepisovatelné kompaktní disky (CD-RW) jsou příklady nosičů s trvalou pamětí.
mód (mode)
Určitý způsob operace v počítačovém programu. Soubory v Pythonu mohou být otevřeny v jednom ze tří módů: číst~read ('r'), psát~write ('w'), připojit~append ('a').
textový soubor (text file)
Soubor, který obsahuje tisknutelné znaky uspořádané do řádků oddělených znaky newline.
adresář či složka (directory or folder)
Pojmenovaná kolekce souborů či dalších adresářů. Adresáře uvnitř adresářů jsou označovány jako podadresáře (subdirectories).
argv
Zkratka pro argument vector a proměnná modulu sys, do které se uloží argumenty příkazového řádku, použité později při běhu programu.

7.10 Cvičení
Napište program mean.py, který na příkazovém řádku konzoly přijme číselné pořadí a vrátí jeho střední hodnotu. Nejde o doctesty.
>>> python mean.py 3 4
3.5
>>> python mean.py 3 4 5
4.0
>>> python mean.py 11 15 94.5 22
35.625
Vztah mezi vstupy a výstupy u vašeho programu by měl být stejný jako v uvedené ukázce.
Při řešení použijete vestavěnou funkci sum:
sum(iterable[, start])

iterable je sekvence číselných hodnot - viz kap. 4.6
[, start] je nepovinná hodnota, která se přičte k součtu
Napište program median.py který na příkazovém řádku přijme číselné pořadí a vrátí jeho prostřední hodnotu. Řešení bude mít nejspíš větev 'if' a 'else'. Budete mít otevřený textový editor a systémovou konzolu, kde budete ověřovat program v souboru plus konzolu Pythonu, kde si budete ověřovat krátká dílčí řešení. Console2 vám ušetří místo na monitoru.
>>> python median.py 3 7 11
7
>>> python median.py 19 85 121
85
>>> python median.py 11 15 16 22
15.5
Proveďte následující:
Spusťte server pydoc příkazem & pydoc -b případně > python -m pydoc -b z příkazového řádku.
Vyberte modul calendar.
Ze sektoru Funkctions vyberte a vyzkoušejte:
>>> import calendar
>>> year = calendar.calendar(2020)
>>> print(year)
Experimentujte s funkcí calendar.isleap(~). Co očekává jako argument? Co vrací jako výsledek? O jaký druh funkce se jedná?
Zapište si poznatky, získané z tohoto cvičení.
Alternativně se lze k webové stránce s nápovědou Pydoc dostat příkazem:

> python -m pydoc -p 7464
To aktivuje webový server pydoc na portu 7464. Jeho stránku ve vašem webovém prohlížeči aktivuje příkaz:

> [b]rowser
Spuštěný server deaktivuje příkaz:
> [q]uit
Použijte tento postup ke spuštění pydoc a vyhledejte modul math.

Kolik funkcí je v modulu math?
Co dělá math.ceil? A co dělá math.floor? (nápověda: jak floor tak ceil očekávají argument v desetinném formátu.)
Popište, jak jsme počítali odmocninu vlastní funkcí sqrt bez použití modulu math.
Jaké jsou datové konstanty v modulu math?
Dělejte si podrobné poznámky o svém zkoumání v tomto cvičení.

Vytvořte modul mymodule1.py. Přidejte atribut myage se zadaným vlastním věkem a year se zadaným současným letopočtem. Vytvořte další modul mymodule2.py. Přidejte atribut myage s nastavenou nulou a year s rokem svého narození.

Nyní vytvořte soubor namespace.py. Importujte oba výše uvedené moduly a napište následující příkaz:
print((mymodule1.myage - mymodule2.myage)
                == (mymodule1.year - mymodule2.year))
Spustíte-li namespace.py, dostanete jako výstup buď True nebo False podle toho, zda jste letos již narozeniny měl nebo neměl.

V prostředí interpretační konzoly si vykoušejte následující:
>>> import this
Co říká Tim Peter o jmenných prostorech?
Použijte pydoc k vyhledání a vyzkoušení dalších funkcí z modulu string. Porovnejte se seznamem, evokovaným příkazy:
>>> import string
>>> dir(string)
Použijte dir(str) a dir(list) k nalezení nejméně tří metod na řetězci a seznamu, které nebyly dosud uvedeny. Prozatím ignorujte všechno, co začíná dvojitým podtržítkem (__). Pečlivě si zapisujte své poznatky včetně jmen nových metod a příkladů jejich použití.
Nápověda: Vytiskněte si dokumentační řetězec funkce, kteru chcete zkoumat. Například, abychom zjistili, jak pracuje str.join, zadáme příkaz print(str.join.__doc__)
V prostředí konzoly vyvolávejte odezvy k následujícím příkazům:
>>> s = "If we took the bones out, \
         it wouldn't be crunchy, would it?"
>>> s.split()
>>> type(s.split())
>>> s.split('o')
>>> s.split('i')
>>> '0'.join(s.split('o'))
Je důležité, abyste každému výsledku porozuměl.
Získané poznatky použijte při doplnění následující funkce s použitím metod split a join na objektech str:
def myreplace(old, new, s ):
    """
    Nahraď všechny argumenty 'old' argumenty 'new'
    v řetězci 's'.

    >>> myreplace(',', ';', 'this, that, and, some, other, thing')
    'this; that; and; some; other; thing'

    >>> myreplace(' ', '**', 'Words will now be separated by stars.')
    'Words**will**now**be**separated**by**stars.'
    """
Vaše řešení má projít oběma doctesty. Tutéž úlohu řešte také přímo s použitím metody replace.
Vytvořte modul wordtools.py s následujcím ukončením:
if __name__ == '__main__':
    import doctest
    doctest.testmod()
Vysvětlete jak tento příkaz usnadňuje užití a testování vytvořeného modulu. Jaká bude hodnota __name__ při importu wordtools.py z jiného modulu? A jaká bude při spuštění wordtools.py jako hlavního programu? Ve kterém případě budou aktivovány doctesty?
Nyní do tohoto souboru postupně přidejte těla ke každé z následujících funkcí tak, aby bylo vyhověno doctestům:
def cleanword(word):
    """
    >>> cleanword('what?')
    'what'
    >>> cleanword('"now!"')
    'now'
    >>> cleanword('?+="word!,@$()"')
    'word'
    """

def has_dashdash(s):
    """
    >>> has_dashdash('distance--but')
    True
    >>> has_dashdash('several')
    False
    >>> has_dashdash('critters')
    False
    >>> has_dashdash('spoke--fancy')
    True
    >>> has_dashdash('yo-yo')
    False
    """

def extract_words(s):
    """
    >>> extract_words('Now is the time!"Now", is the time? Yes, now.')
    ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
    >>> extract_words('she tried to curtsey as she spoke--fancy')
    ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """


def wordcount(word, wordlist):
    """
    >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['now', 2]
    >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
    ['is', 4]
    >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['time', 1]
    >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['frog', 0]
    """


def wordset(wordlist):
    """
    >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['is', 'now', 'time']
    >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
    ['I', 'a', 'am', 'is']
    >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
    ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """


def longestword(wordset):
    """
    >>> longestword(['a', 'apple', 'pear', 'grape'])
    5
    >>> longestword(['a', 'am', 'I', 'be'])
    2
    >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
    34
    """

Modul si uložte pro použití jeho procedur v jiných programech.
Upravte program countLetters_acc.py ze cvičení 6.19.2 tak aby jméno souboru a potřebné argumenty mohly být přijaty z příkazového řádku. Řešení si uložte do souboru countLetters_cli.py.
previous up next  hi end   end


# ================================
miko oddel
# ================================
8. Seznamy I
# ================================


Vytvoření seznamu
Přístup k položkám
Délka seznamu
Operace se seznamy
Úseky seznamu
Seznamy jsou měnitelné
Smazání položek
Kopírování objektů
Seznamy a smyčky 'for'
Komprehence
Glosář
Cvičení
Seznam (list) je uspořádaná sekvence hodnot libovolného typu. Jednotlivým hodnotám říkáme položky a tyto položky jsou měnitelné.
Položkou seznamu může být i další seznam. Takový seznam se nazyvá vnořený seznam.


8.1 Vytvoření seznamu
Taxativním výčtem
Nový seznam vytvoříme nejjednodušeji uzavřením položek do hranatých závorek:

[10, 20, 30, 40]
["spam", "bungee", "swallow"]
Prvním příkladem je seznam čtyř celých čísel. Druhým je seznam tří řetězců. Položky seznamu nemusí být stejného typu. Následující seznam obsahuje řetězec, float, integer a (mirabile dictu!) další seznam:

["hello", 2.0, 5, [10, 20]]
Seznamu uvnitř jiného seznamu říkáme, že je vnořený.

Konečně, existuje speciální seznam, který neobsahuje žádné položky. Nazývá se prázdný seznam a značí se [ ].

Stejně jako číselná hodnota 0 a prázdný řetězec, je prázdný seznam nepravdivý v booleovských výrazech:.

>>> bool(["hello", 2.0])
True
>>> bool([])
False
>>>
Vytvořený seznam můžeme samozřejmě přiřadit k proměnné nebo zadat jako parametr či argument funkce.

>>> vocabulary = ["ameliorate", "castigate", "defenestrate"]
>>> numbers = [17, 123]
>>> empty = []
>>> print(vocabulary, numbers, empty)
['ameliorate', 'castigate', 'defenestrate'] [17, 123] []
Funkcí list()
Funkce list(~) vytvoří seznam a jako argument přijímá hodnoty typu str, bytes, bytearray, tuple, range, dict, set, frozenset, neboli všechny kontejnery (sekvence a kolekce), zadané jako jeden argument. Společnou vlastností argumentů je to, že to jsou všechno iterábly - viz Kap. 4.6.

>>> list("osel")                         # typ str
['o', 's', 'e', 'l']
>>> list(b"osel")                        # typ bytes
[111, 115, 101, 108]
>>> list(("a", 5, True))                 # typ tuple
['a', 5, True]
>>> list(range(4))                       # typ range
[0, 1, 2, 3]
>>> list({"a", 5, True})                 # typ set
[True, 5, 'a']
>>> list({"a":2, "b":False, "c":"d"})    # typ dict
['a', 'b', 'c']
Převod řetězce na seznam s manipulací lze provést metodou split - viz kapitola 9.1

Komprehencí seznamu
Komprehenci (viz odstavec 8.10) použijeme hlavně při úpravě stávajícího seznamu.


8.2 Přístup k položkám
Syntaxe pro přístup k položkám seznamu je stejná jako syntaxe pro přístup ke znakům řetězce – pomocí hranatých závorek s indexem. Nezapomeňte, že indexy začínají nulou:

>>> nested = ["hello", 123, [10,20]]
>>> print(nested[1])
123
Jako index lze použít jakýkoli celočíselný výraz:

>>> nested[9-8]                #  == 1
123
>>> nested[1.0]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: list indices must be integers
Pokusíme-li se číst nebo psát položku, která neexistuje, dostaneme chybu při běhu programu:

>>> nested[3]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
IndexError: list index out of range
Má-li index zápornou hodnotu, počítá se od konce seznamu:

>>> nested[-1]
[10, 20]
>>> nested[-3]
'hello'
>>> numbers[-4]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
IndexError: list index out of range
numbers[-1] je poslední položka seznamu, numbers[-4] zde neexistuje.
Pro prvek vnořeného seznamu uvedeme rovněž jeho index:

>>> nested[2][1]
20
Je obvyklé použít proměnnou jako index seznamu:

horsemen = ["war", "famine", "pestilence", "death"]

i = 0                  # proměnná pro smyčku - počítadlo
while i < 4:
    print(horsemen[i], end=" ")
    i = i + 1
Tato smyčka počítá od 0 do 4. Jakmile má proměnná hodnotu 4, podmínka nevyhoví a smyčka končí. Takže tělo smyčky je provedeno pro i = 0, 1, 2 a 3.

Při každém cyklu smyčky je proměnná i použita jako index položky, která se tiskne. Tento způsob výpočtu se nazývá traverzování seznamem.


8.3 Délka seznamu
Funkce len vrací délku seznamu, což je počet jeho položek. Tato hodnota se výhodně používá jako horní mez smyčky místo konstanty. Tím si zajistíme, že pokaždé, když se změní velikost seznamu, nemusíme procházet programem, abychom opravili všechny dotčené smyčky:

horsemen = ["war", "famine", "pestilence", "death"]

i = 0
while i < len(horsemen):
    print( horsemen[i], end=" ")
    i = i + 1
Po posledním provedením těla smyčky je i=len(horsemen)-1, což je index poslední položky. Je-li i=len(horsemen), podmínka není splněna a tělo se neprovede.

I když jeden seznam může obsahovat další seznam, ten vnořený se stále počítá jako jedna položka. Délka tohoto seznamu je 4:

['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
Traverzování i vnořeným seznamem popisuje text kap. 13.2.


8.4 Operace se seznamy
Společné operace pro seznamy a řetězce
U seznamu lze uplatnit stejné operace jako u řetězců - viz 6.5.1

Operátor + zřetězí seznamy:

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print( c )
[1, 2, 3, 4, 5, 6]
Podobně, operátor * opakuje seznam v zadaném počtu:

>>> [0]*4
[0, 0, 0, 0]
>>> [1, 2, 3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
První příklad opakuje [0] čtyřikrát. Druhý příklad opakuje seznam [1, 2, 3] třikrát.

Vestavěné metody a funkce pro seznamy
Pro seznamy neexistuje modul list jako existuje modul string pro řetězce.

Podrobnosti o metodách nejlépe zjistíme na stránce List Methods & Functions nebo programiz.com, kde nalezneme popis skladby i s příklady pro tyto metody a funkce:

Metody
append, extend, index, insert, clear, copy, count, pop,
remove, reverse, sort, split       jsou společné i pro řetězce

Funkce
len, max, min                      jsou společné pro všechny iterábly
list
Příslušnost položky
Klíčové slovo in je booleovský operátor, který testuje příslušnost prvku k sekvenci. Použili jsme jej už u řetězců a pracuje také se seznamy a s jinými uspořádanými množinami:

>>> horsemen = ['war', 'famine', 'pestilence', 'death']
>>> 'pestilence' in horsemen
True
>>> 'debauchery' in horsemen
False
Protože pestilence je částicí seznamu horsemen, vrátí operátor in hodnotu True. Jelikož debauchery v seznamu není, vrátí False.

Můžeme použít slovo not ve spojení s in, abychom ověřili, že položka není částicí seznamu:

>>> 'debauchery' not in horsemen
True

8.5 Úseky seznamu
Operace s úseky, které jsme poznali u řetězců, platí také u seznamů:

>>> a_list = ['a', 'b', 'c', 'd', 'e', 'f']
>>> a_list[1:3]
['b', 'c']
>>> a_list[:4]
['a', 'b', 'c', 'd']
>>> a_list[3:]
['d', 'e', 'f']
>>> a_list[:]
['a', 'b', 'c', 'd', 'e', 'f']

8.6 Seznamy jsou měnitelné
Na rozdíl od řetězců jsou seznamy měnitelné, což znamená, že můžeme měnit jejich položky. Použitím závorkového operátoru [ ] můžeme měnit hodnotu položek:

>>> fruit = ["banana", "apple", "quince"]
>>> fruit[0] = "pear"
>>> fruit[-1] = "orange"
>>> print(fruit)
['pear', 'apple', 'orange']
Přiřazení hodnoty položce stringu se nazývá položkové přiřazení (item assignment). Takovéto přiřazení nejde použít u řetězců:

>>> 'TEST'[2] = 'X'
Traceback (most recent call last):
  File "<stdin >", line 1, in <module >
TypeError: 'str' object does not support item assignment
ale je podporováno u seznamu řetězců:

>>> my_list = ['T', 'E', 'S', 'T']
>>> my_list[2] = 'X'
>>> my_list
['T', 'E', 'X', 'T']
Úsekovým operátorem můžeme změnit několik položek najednou:

>>> a_list = ['a', 'b', 'c', 'd', 'e', 'f']
>>> a_list[1:3] = ['x', 'y']
>>> print(a_list)
['a', 'x', 'y', 'd', 'e', 'f']
Můžeme také odstranit položky ze seznamu tím, že je nahradíme prázdným seznamem:

>>> a_list = ['a', 'b', 'c', 'd', 'e', 'f']
>>> a_list[1:3] = []
>>> print(a_list)
['a', 'd', 'e', 'f']
A můžeme také přidat položky do seznamu vmáčknutím do prázdného úseku v potřebném místě:

>>> a_list = ['a', 'd', 'f']
>>> a_list[1:1] = ['b', 'c']
>>> print(a_list)
['a', 'b', 'c', 'd', 'f']
>>> a_list[4:4] = ['e']
>>> print(a_list)
['a', 'b', 'c', 'd', 'e', 'f']

8.7 Smazání položek
Použití úseků k výmazu položek je neohrabané a proto náchylné k chybám. Python poskytuje šikovnější alternativu.

Příkaz del odstraní položku ze seznamu:

>>> a = ['one', 'two', 'three']
>>> del a[1]
>>> a
['one', 'three']
Nepřekvapí nás, že del manipuluje také se zápornými indexy a vyvolá chybu při běhu programu, je-li index mimo dovolený rozsah.

Jako indexy pro del můžeme použít také úseky:

>>> a_list = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del a_list[1:5]
>>> print(a_list)
['a', 'f']
Jako obvykle, úseky vyberou všechny položky zadaného rozsahu, kromě horní meze.


8.8 Kopírování objektů
Účelem kopírování je vytvoření nezávislé, autonomní kopie objektu. Tuto kopii lze provést jako mělkou (shallow) nebo důkladnou (deep).

Rozhodující vlastností kopírovaného objektu je jeho složení. Jednoprvkový objekt nebo jednoduché prvky kontejneru (list, tuple, set, dict) lze nezávisle reprodukovat jako shallow copy. Kontejner s vnořenými složenými prvky lze nezávisle reprodukovat pouze jako deep copy.
Za kopii nelze považovat přiřazení téhož objektu k více proměnným - viz alias.

Zdánlivá kopie - alias
Zdánlivou kopii neboli alias vytvoříme přiřazením téhož objektu k více jménům, což lze provést najednou v jednom řádku:

>>> a = b = [1, 2, 3]
>>> id(a), id(b), id([1, 2, 3])
(59931496, 59931496, 59931400)
nebo postupně

>>> orig = [2, [True, False], "asi"]        # prosté přiřazení
>>> kopie = orig                            # kopie přiřazením (alias)
>>> id(orig), id(kopie), id([2, [True, False], "asi"])
(59931464, 59931464, 59931688)
Schema vztahů může vypadat takto:



Proměnné se shodnými ID odkazují na stejný objekt. Změny objektu provedené prostřednictvím jednoho aliasu se projeví i u dalšího aliasu:

>>> b[0] = 5
>>> a
[5, 2, 3]
Mělká kopie
Při mělké (shallow) kopii se v možném rozsahu vytvoří nový samostatný klon originálu. Mělkou kopii můžeme provést čtverým způsobem - například pro seznam:

>>> orig = [2, [True, False], "asi"]
Použitím vestavěné metody copy():

>>> orig_shall_one = orig.copy()
Konverzí seznamu na entici (případně obráceně):

>>> orig_shall_two = list(orig)
Použitím úsekového operátoru:

>>> orig_shall_three = orig[:]
Použitím metody copy z modulu copy:

>>> import copy
>>> orig_shall_four = copy.copy(orig)
Ve všech čtyřech uvedených případech se nezávisle kopírují pouze jednoduché členy kopírovaného seznamu. Prvky vloženého seznamu jsou závisle propojeny se svým originálem:

>>> orig[2] = "yes"; orig[1][1] = 8
>>> orig_shall_three; orig
[2, [True, 8], 'asi']               # orig_shall_three
[2, [True, 8], 'yes']               # orig
Hluboká kopie
Při hluboké (deep) kopii složeného objektu se vytvoří nový složený objekt, do něhož se vkládají nezávislé kopie objektů, nalezených v originálu.
Hlubokou kopii vytvoříme importovanou metodou deepcopy z modulu copy:

>>> from copy import deepcopy
>>> orig_deep = deepcopy(orig)
>>> orig[2] = "snad"; orig[1][1] = True
>>> orig_deep; orig
[2, [True, False], 'asi']               # orig_deep
[2, [True, True], 'snad']               # orig

8.9 Seznamy a smyčky 'for'
Interní mechanizmus smyčky for - viz kap 4.7. Použití smyčky for je velmi rozmanité, např.:

fruit = ["banana", "apple", "quince"]           # proveďte v IDLE
for ovoce in fruit:
    print("I like to eat " + ovoce + "s!")
Měnitelnost seznamu nám umožňuje při jeho procházení (traverzování) upravit každou jeho položku. Následující kód vytvoří druhé mocniny čísel od 1 do 3:

numbers = [1, 2, 3]
for elem in range(len(numbers)):
   print(numbers[elem], "-->", numbers[elem]**2, end =", ")
Výstup v IDLE:

======== RESTART: F:/Codetest/HowTo/trump_one.py ========
1 --> 1, 2 --> 4, 3 --> 9,
Zamyslete se nad příkazem range(len(numbers)) a snažte se pochopit, jak tento příkaz pracuje. Uvnitř seznamu nás zajímá jak původní hodnota položky, tak i její změněná hodnota.

Funkce enumerate generuje při traverzování seznamem jak index, tak i odpovídající hodnotu. Pro lepší pochopení práce příkazu enumerate si vyzkoušejte následující příklad:

>>> for index, value in enumerate(['banana', 'apple', 'pear']):
...     print(index, value )
...
0 banana
1 apple
2 pear
>>>
Jiné příklady využití funkce enumerate() - viz kap. 4.9.


8.10 Komprehence
Komprehence je skladebný předpis pro vytvoření seznamu, setu či entice z poskytnutého objektu typu list, tuple, string, bytes, dict s použitím kompaktního předpisu, případně ještě při splnění jisté (avšak nepovinné) podmínky.

Komprehenci lze ilustrovat matematickým výrazem:

S = { 2*x | x € N, x² > 3 }
jenž lze slovně interpretovat asi takto: Pro všechna x z oboru přirozených čísel N jejichž druhé mocniny jsou větší než 3 se provede výraz 2*x.
V jazyce Python lze uvedený výraz vyjádřit konstrukcí, kterou si označíme jako komprehence seznamu:

>>> kompr = [f(x) for x in <objekt> if <podmínka>]
případně jako komprehence setu:
>>> kompr = {f(x) for x in <objekt> if <podmínka>}
Jak vidno, rozdíl mezi komprenencí seznamu a komprehencí setu spočívá pouze v použitých závorkách. Pro komprehenci entice bychom použili kulaté závorky.

Ukažme si výše uvedený obecný matematický výraz převedený do komprehence seznamu a setu (prozatím bez podmínky):

>>> numbers = [1, 2, 3, 4]
>>> [x**2 for x in numbers]        # komprehence seznamu ze seznamu
[1, 4, 9, 16]
>>> {x**2 for x in numbers}        # komprehence setu ze seznamu
{16, 1, 4, 9}
>>> (x**2 for x in numbers)        # komprehence entice ze seznamu
<generator object <genexpr> at 0x0343B680>
Komprehence entice (tuple) vytváří generátorový objekt, jímž se budeme zabývat v kap. 13.5.


Dále si ukážeme komprehenci s podmínkou:
>>> [x**2 for x in numbers if x**2 > 3]
[4, 9, 16]                             # komprehence seznamu ze seznamu
>>>
>>> files = ('bin', 'Data', 'Desktop', '.bashrc', '.ssh', '.vimrc')
>>> [name for name in files if name[0] != '.']
['bin', 'Data', 'Desktop']             # komprehence seznamu z entice
Výrazových předpisů může být v jedné komprehenci více:
>>> [(x, x**2, x**3) for x in numbers]   # komprehence seznamu ze seznamu
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]
# ohraničení výrazu v zadání určuje ohraničení elementů ve výstupu
# nahraďte kulaté závorky v zadání složenými a proveďte vyhodnocení vstupu
Může být více i poskytnutých objektů:
>>> numbers = (1, 2, 3, 4)
>>> letters = ['a', 'b', 'c']
>>> [n*letter for n in numbers for letter in letters]
['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc']
Zajímavá je úprava argumentu v této komprehenci:

>>> [v*2 for v in ("a", 5, True)]
['aa', 10, 2]                                 # 2*True = 2*1 = 2
Za povšimnutí stojí i toto spojení komprehence s formátováním řetězce dle kap. 6.16:

>>> boys = ["Pavel", "Petr", "Jan"]
>>> synci = ["{} Novotný".format(boy) for boy in boys]
>>> synci
['Pavel Novotný', 'Petr Novotný', 'Jan Novotný']
Ukázka komprehence setu z řetězce:

>>> s = {v for v in "ABCDABCD" if v not in "CB"}
>>> s
{'A', 'D'}
Komprehencí setu z řetězce lze s pomocí funkce enumerate (kap. 4.9) vytvořít výběrový slovník:
>>> d = {key:val for key,val in enumerate ('ABCD') if val not in "CB"}
>>> d
{0: 'A', 3: 'D'}
Zajímavé je použití pojmenovaného výrazu (mroží operátor - 2.8.6) při komprehenci seznamu:

>>> def f(x):
...    return x + 2

>>> print([[y := f(x), x/y] for x in range(3)])
[[2, 0.0], [3, 0.3333333333333333], [4, 0.5]]

případně s podmínkou a přehledněji:
>>> print([(x, y, x/y) for x in range(3) if (y := f(x)) > 0])
[(0, 2, 0.0), (1, 3, 0.3333333333333333), (2, 4, 0.5)]
Následující komprehencí vybereme ze zadané množiny bodů ty, které leží uvnitř kružnice o poloměru r = 2:

>>> import math
>>> radius = 2
>>> [(x, y) for x in range(-2,3) for y in range(-2,3) if
...  math.sqrt(x**2 + y**2) < radius]
[(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

8.11 Glosář
seznam (list)
Měnitelná kolekce objektů (případně různého typu), kde každý objekt je označen indexem.
položka (element)
Jedna z hodnot seznamu (nebo jiné sekvence). Operátor z hranatých závorek vybere položku ze seznamu.
sekvence (sequence)
Jakýkoliv datový typ, skládající se z uspořadané řady položek, kde každá položka je určena indexem.
vnořený seznam (nested list)
Seznam, který je položkou jiného seznamu.
krok (step)
Interval mezi sousedními položkami v lineární sekvenci. Také třetí (a nepovinný) argument fce range. Není-li zadán, jeho implicitní hodnotou je 1.
traverzování seznamem (list traversal)
Postupný výběr každé položky seznamu.
alias
Vícero proměnných, odkazujících na stejný objekt.
klonovat (clone)
Vytvořit nový objekt, který má stejnou hodnotu jako stávající objekt. Kopírování odkazu na objekt vytvoří alias, nikoliv klon.
komprehence seznamu (list comprehension)
Určení položek seznamu nikoliv jejich výčtem ale popisem jejich vlastností.
oddělovač (separator, delimiter)
Znak nebo řetězec použitý k označení místa, kde má být jiný řetězec rozdělen.

8.12 Cvičení
Napište smyčku, která traverzuje seznamem:
['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
a vytiskne délku každé položky. Co se stane, zadáme-li funkci len jako argument celé číslo?
Vytvořte soubor doctests.py do něhož budeme postupně přidávat úlohy ad a, b, c, d podle následující šablony:
# zde napište zadání úlohy
"""
# zde překopírujte doctest úlohy
"""
# zde napište řešení úlohy
Podle naznačených výsledků sestavte možnou hodnotu seznamu a_list:

"""
   >>> a_list[3]
   42
   >>> a_list[6]
   'Ni!'
   >>> len(a_list)
   8
"""
Podle naznačených výsledků sestavte možnou hodnotu seznamu b_list a c_list:

"""
   >>> b_list[1:]
   ['Stills', 'Nash']
   >>> group = b_list + c_list
   >>> group[-1]
   'Young'
"""
Podle naznačených výsledků sestavte možnou hodnotu seznamu mystery_list:

"""
   >>> 'war' in mystery_list
   False
   >>> 'peace' in mystery_list
   True
   >>> 'justice' in mystery_list
   True
   >>> 'oppression' in mystery_list
   False
   >>> 'equality' in mystery_list
   True
"""
Vytvořte funkci list_range s naznačeným výstupem:

"""
   >>> list_range(a, b, c)
   [5,9,13,17]
"""
Tři argumenty pro funkci range jsou start, stop, step. Co se stane, když start < stop a step < 0 ?
>>> range(10, 0, -2)
Po opětovném prostudování odstavce 4.8 napište funkci my_range(...), která vrátí výpis prvků range(a,b,c).

Nakreslete schematické zobrazení vztahu mezi a, b před provedením třetího řádku a po jeho provedení.
a = [1, 2, 3]
b = a[:]
b[0] = 5
Jaký bude výstup následujícího programu?
this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crook']
print("Test 1: %s" % (id(this) == id(that)))
that = this
print("Test 2: %s" % (id(this) == id(that)))
Přidejte podrobné vysvětlení výsledků.

Následující tři úlohy zapište do souboru dedukce.py. Doctest při tom nebudete potřebovat.
Určete hodnoty proměnných junk, a, b tak, aby po naznačených úkonech měl seznam junk hodnotu stejnou jako na posledním řádku:

"""
   >>> 13 in junk
   True
   >>> del junk[4]
   >>> junk
   [3, 7, 9, 10, 13, 17, 21, 24, 27]
   >>> del junk[a:b]
   >>> junk
   [3, 7, 27]
"""
Nakreslete schema seznamu nlist, do kterého doplníte dále uvedené hodoty 0, 17, 5:

"""
   >>> nlist[2][1]
   0
   >>> nlist[0][2]
   17
   >>> nlist[1][1]
   5
"""
Podle výstupu z metody .split() sestavte hodnotu proměnné retiazka:

"""
   >>> retiazka.split()
   ['this', 'and', 'that']
"""
Napište funkci add_lists(a,b) která přijme dva seznamy stejné délky s celými čísly a vrátí nový seznam se součty odpovídajících položek.
def add_lists(a, b):
    """
    >>> add_lists([1,1], [1,1])
    [2, 2]
    >>> add_lists([1,2], [1,4])
    [2, 6]
    >>> add_lists([1,2,1], [1,4,3])
    [2, 6, 4]
    """
Fce add_lists musí být ve shodě s uvedenými doctesty.

Napište funkci mult_lists(a, b) která přijme dva seznamy stejné délky s celými čísly a vrátí součet součinů odpovídajících položek.
def mult_lists(a, b):
    """
    >>> mult_lists([1,1], [1,1])
    2
    >>> mult_lists([1,2], [1,4])
    9
    >>> mult_lists([1,2,1], [1,4,3])
    12
    """
Ověřte si, že fce mult_lists vyhovuje uvedeným doctestům.

Vyzkoušejte si různé separátory u funkcí join a split.
Napište funkci replace(s, old, new), která zamění všechny výskyty old za new v řetězci s.
def replace (s, old, new):
    """
    >>> replace ('Mississippi','i', 'I')
    'MIssIssIppI'
    >>> s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
    >>> replace(s, 'om', 'am')
    'I love spam! Spam is my favorite food. Spam, spam, spam, yum!'
    >>> replace(s, 'o', 'a')
    'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!'
    """
Řešení musí zajisté vyhovovat doctestům. Použije se split a join.
Uveďte odezvy konzoly na následující zápisy:
>>> nums = [1, 2, 3, 4]
>>> [x**3 for x in nums]
>>> nums = [1, 2, 3, 4]
>>> [x**2 for x in nums if x**2 != 4]
>>> nums = [1, 2, 3, 4]
>>> [(x, y) for x in nums for y in nums]
>>> nums = [1, 2, 3, 4]
>>> [(x, y) for x in nums for y in nums if x != y]
Měl byste předjímat výsledky předtím, než vám je ukáže konzola interpreta.
previous    up  next    hi  end end

# ================================
miko oddel
# ================================
9. Seznamy II
# ================================

Metody 'split' a 'join'
Matice
Modul Numpy
Testem podnícený rozvoj
Náhodná čísla
Náhodný výběr
Seznam náhodných čísel
Četnost
Vytvoření úseků
Matplotlib
Glosář
Cvičení
9.1 Metody 'split' a 'join'
Umíme z řetězce vytvořit seznam (list(arg)) a ze seznamu řetězec (str(arg)), dokonce to umíme udělat jedním tahem:

>>> str (list("Žabička"))
"['Ž', 'a', 'b', 'i', 'č', 'k', 'a']"
Chceme-li z rozsypaného čaje sestavit zase žabičku, musíme použít funkci join :

>>> frog = list("Žabička")
>>> frog
['Ž', 'a', 'b', 'i', 'č', 'k', 'a']
>>> "".join(frog)
'Žabička'
>>>
Funkce split rozloží řetězec na seznam slov:

>>> song = "The rain in Spain..."
>>> song.split()
['The', 'rain', 'in', 'Spain...']
>>>
Vhodně vybraný argument, nazvaný oddělovač (separátor), může být použit jako hranice mezi oddělenými úseky. Následující příklad používá jako oddělovač řetězec ai:

>>> song.split(sep='ai')
['The r', 'n in Sp','n...']
Případně:
>>> "abrakadabra".split("a", 2)
['', 'br', 'kadabra']
Všimněte si, že zadaný separátor se ve vytvořeném seznamu neobjevuje.

Metoda join  i  split přijímá dva argumenty: seznam řetězců a hodnotu separátoru. Implicitní hodnotou separátoru u metody split je mezera: split().

>>> words = ['crunchy', 'raw', 'unboned', 'real', 'dead', 'frog']
>>> " ".join(words)
'crunchy raw unboned real dead frog'
>>> "**".join(words)
'crunchy**raw**unboned**real**dead**frog'

9.2 Matice
K vyjádření matic se často používají vnořené seznamy. Například, matice o rozměru 3x3 (3 řádky x 3 sloupce):



může být vyjádřena jako seznam s vnořenými seznamy stejné délky. Jednotlivé vnořené seznamy prezentují příslušné řádky matice:

>>> matrix = [[1, 2, 3],
...           [4, 5, 6],
...           [7, 8, 9]]

Tentýž zápis v úspornějším provedení:
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
V maticovém počtu lze tyto vnořené seznamy označit jako řádkové matice, neboli vektory.

Řádek matice vybereme jako prvek vnějšího seznamu (indexy počínají nulou):

>>> matrix[1]
[4, 5, 6]
Položku určitého řádku označíme indexem řádku a indexem položky:

>>> matrix[1][1]
5
Práce s maticemi vyžaduje specifické znalosti maticového počtu. Na rozdíl od algebry v něm například obecně neplatí komutativní zákon: A*B != B*A; platí ale A+B == B+A.

Násobení matice A o velikosti m (řádků) x n (sloupců) maticí B o velikosti n (řádků) x p (sloupců) je možné v případě, že počet sloupců (n) matice A souhlasí s počtem řádků (n) matice B. Rozměr výsledné matice je m x p.

Pokud je tato podmínka splněna, lze prvek c(i,j) matice C = A*B určit jako algebraický součet součinů prvků z i-tého řádku matice A s prvky z i-tého sloupce matice B, jak je naznačeno v tomto schematu:

| 1 2 | * | 5 6 |     1*5 + 2*7 | 1*6 + 2*8     | 19 22 |
|     |   |     |  =  ----------|----------  =  |       |
| 3 4 |   | 7 8 |     3*5 + 4*7 | 5*6 + 4*8     | 43 50 |
Rozměr výsledné matice ab je tedy dán počtem řádků matice a ( m rows = len(a)) a počtem sloupců matice b (p cols = len(b[0])).

a = [[1, 2, 3], [4, 5, 6]]              # 2 řádky, 3 sloupce:   a(2,3)
b = [[7, 8], [9, 2], [3,1]]             # 3 řádky, 2 sloupce:   b(3,2)
ab = a * b = [[34, 15], [91], [48]]     # 2 řádky, 2 sloupce:  ab(2,2)

# ab(0,0)= 1*7 + 2*9 + 3*3 = 34
# ab(1,1)= 4*8 + 5*2 + 6*1 = 48
Výpočet součinu matic lze provést trojím použitím idiomu for i in range(len(...)):

def matrix_mult (m1, m2):
    result = [[0 for row in range(len(m1))]     # maketa matice
                 for col in range(len(m2[0]))]
    for i in range(len(m1)):                    # rows in m1
        for j in range(len(m2[0])):             # cols in m2
            for k in range(len(m2)):            # rows in m2

                result[i][j] += m1[i][k] * m2[k][j]
    return result
========= RESTART: F:\Codetest\HowTo\matice\Test.py ========
>>> a = [[1,2,3], [4,5,6]]
>>> b = [[7,8], [9,1], [2,3]]
>>> matrix_mult(a,b)
[[31, 19], [85, 55]]
Sevřenější tvar má toto řešení s komprehencí seznamu a s vestavěnými funkcemi sum a zip:

def matrix_mult (m1, m2):
    # interní pojmenování: m1_r, m2_c
    # *m2 je sběrný parametr (sloupec druhé matice)

    return [[sum(x * y
             for x, y in zip(m1_r, m2_c))
             for m2_c in zip(*m2)]
             for m1_r in m1]
Nejsnazší práci s maticemi poskytuje modul NumPy.


9.3 Modul Numpy
Aplikaci Numpy je nutné nejprve instalovat. Ve Windows s instalovaným programem Python s aplikací pip to je jednoduché:

C:\> pip install numpy
Knihovnu Numpy je nutné importovat do aktuálního pracovního prostředí Pythonu:

>>> import numpy as np
Numpy používá vlastní formát kolektoru, zvaný array neboli pole. Prvky tohoto kolektoru musí být homogenní - to jest, musí být stejného typu.
Datový typ pole může být jedno- (1D, vektor), dvě- (2D, matice), tři- (3D, tenzor) i více (nD) dimenzionální.
Dimenzím se v Numpy říká osy (axes). Velikost pole je vyjádřen atributem shape (tvar), což je entice celých čísel, která vyjadřují délky jednotivých os (dimenzí).

Array v Numpy vytvoříme ze seznamu příkazem np.array() :

>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
>>> a[1][2]
7
>>> a.shape
(2,4)                   # počet os = počtu prvků v entici
Uvedené pole má dvě osy (je to tedy matice) o délkách 2 a 4 položky. Pro přístup k vybranému prvku matice lze použít indexy (počínající nulou).

Součin dvou matic je v Numpy líbezně prostý:
>>> a = np.array([[1,2,3], [4,5,6]])
>>> b = np.array([[7,8], [9,1], [2,3]])
>>> c = np.matmul(a, b)
>>> c.shape
(2, 2)
>>> print(c)
[[31, 19],
 [85, 55]]
Protože solidnější popis práce s modulem Numpy přesahuje rámec tohoto tutoriálu, odkazuji případné zájemce na tuto webovou stránku.


9.4 Testem podnícený rozvoj
Testem podnícený rozvoj (Test-driven development - TDD) je způsob vyvíjení programu, při kterém se postupuje po malých, automaticky ověřovaných krocích.

Tento postup si ukážeme na sestavení funkce, která vytvoří matici m * n  (rows krát columns). Při tomto postupu použijeme doctesty, které jsme poznali již v odstavci 4.8.

Nejprve pro tuto funkci sestavime test a uložíme do souboru ch09_matrices.py:

def make_matrix (rows, columns):
    """
    >>> make_matrix(3,5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    """

if  __name__ == '__main__':
    import doctest
    doctest.testmod()
Provedení skriptu skončí neúspěchem:

********************************************************
File "matrices.py", line 3, in __main__.make_matrix
Failed example:
    make_matrix(3, 5)
Expected:
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Got nothing
********************************************************
1 items had failures:
   1 of   1 in __main__.make_matrix
***Test Failed*** 1 failures.
Test nebyl úspěšný proto, že tělo funkce obsahuje pouze dokumentační řetězec a žádný příkaz return, takže je vráceno Got nothing. Náš test nám naznačuje, že jsme chtěli vrátit matici se samými nulami ve třech řadách a pěti sloupcích.

Při použití TDD zpravidla píšeme ten nejjednodušší kód, který projde testem, v našem případě to je příkaz return:

def make_matrix (rows, columns):
    """
    >>> make_matrix(3,5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    """
    return [[0, 0, 0, 0, 0], [0, 0,0, 0, 0], [0, 0, 0, 0, 0]]
Při provedení tohoto skriptu rovněž neobstojíme i když dostáváme nominálně stejný ale formálně různý výsledek, lišící se v tom, že citované seznamy jsou různě dlouhé, ten druhý je delší o mezery mezi jednotlivými položkami - doctesty se někdy chovají podivně.

Doplníme tedy mezery do seznamu v dokumentačním řetězci a spuštěním skriptu si ověříme, že tentokrát je všechno v pořádku (no response)
Rozteče argumentů příkazu return upravovat nemusíme, příkaz si je upraví sám.

Uvědomíme si ale, že funkce make_matrix vrací stále týž výsledek, což zajisté není to, co jsme zamýšleli. Ověříme si to přidáním dalšího testu:

def make_matrix (rows, columns):
    """
    >>> make_matrix(3,5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> make_matrix(4,2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Vida:

*********************************************************
File "matrices.py", line 5, in __main__.make_matrix
Failed example:
    make_matrix(4, 2)
Expected:
    [[0, 0], [0, 0], [0, 0], [0, 0]]
Got:
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
*********************************************************
1 items had failures:
   2 of   2 in __main__.make_matrix
***Test Failed*** 1 failures.
Tato technika se nazývá testem podnícená, protože se snažíme upravovat kód tak, abychom prošli testem. Motivováni nezdařeným pokusem, můžeme nyní zkusit obecnější řešení:

def make_matrix (rows, columns):
    """
    >>> make_matrix(3,5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> make_matrix(4,2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0]* columns]* rows
Řešení formálně neuspokojí proceduru doctestu. Jevově jsou oba řádky stejné ale interně se budou zřejmě lišit počtem připojených (neviditelných) mezer. Řekněmež, že nám to nevadí.

Alternativní řešení téže úlohy má tuto skladbu:

def make_matrix (rows, columns):
    """
    >>> make_matrix(3,5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> make_matrix(4,2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    matrix = []
    for row  in range(rows):
        matrix += [[0]* columns]
    return matrix
Použití TDD nám při našem programátorském snažení přináší několik výhod:

pomáhá nám konkrétně přemýšlet o problému před tím, než se jej pokusíme řešit
pobízí nás k rozložení složitého problému do menších, jednodušších úloh, postupně řešitelných
vhodně rozvinutý testovací aparát usnadňuje pozdější přídavky a vylepšení
Funkci make_matrix(r,c) můžeme použít v cvičení 9.11.2 pro vytvoření výchozí (nulové) matice při sčítání (odčítání) matic:

def add_matrix (m1, m2):
   mx = make_matrix(len(m1), len(m1[0]))

9.5 Náhodná čísla
Většina počítačových programů provádí při každém spuštění totéž, takže říkáme, že jsou deterministické.

Determinismus je obvykle dobrá věc, protože můžeme předpokládat, že stejný výpočet povede ke stejnému výsledku. U některých aplikacích si však přejeme, aby počítač byl nepředvídatelný. Hry jsou zřejmým příkladem, ale těch příkladů může být více.
Ukazuje se, že napsat program se skutečně nepředvídatelným chováním není snadné, ale jsou způsoby, kterak jej učinit alespoň zdánlivě nedeterministickým. Jedním ze způsobů je použití náhodných čísel. Python poskytuje vestavěnou funkci, která generuje pseudonáhodná čísla, která nejsou náhodná v přísně matematickém smyslu, ale pro naše účely postačí.

Modul random obsahuje funkci zvanou random, která vrací desetinné číslo v rozsahu [0.0, 1.0). Pokaždé, když voláme funkci random, dostaneme jednu "náhodnou" hodnotu mezi nulou včetně a méně než jedničkou. Více náhodných hodnot můžeme vygenerovat pomocí funkce se smyčkou:

import random
def rand(high):   # high is an integer
    for i in range(high):
        x = random.random()
    print(x*high)
Náhodná čísla mezi nulou a zadanou mezí high, získáme násobením generovaných čísel x hodnotou high.

9.6 Náhodný výběr
Podobným problémem jako vytvoření náhodného čísla je provedení náhodného výběru. Ten lze provést pomocí funkce choice z modulu random:

>>> from random import choice
>>> fokus = ["asi", "jo", ("a"*3),  [12, sum], "pět"]
>>> choice(fokus)
[12, < built-in function sum>]
>>> choice(fokus)
'jo'
Jak vidno, elementy výběrového seznamu (nebo entice či setu) mohou být hodnoty různého typu.

9.7 Seznam náhodných čísel
V prvním kroku vygenerujeme seznam náhodných čísel funkcí randomList. Funkce přijme jako argument celé číslo n a vrátí seznam náhodných čísel. Začíná se seznamem s n nulami. Při každém cyklu smyčky se jedna z položek nahradí náhodným číslem. Výstupní hodnotou je odkaz na dokončený seznam.
Parametr n je požadovaný počet náhodných čísel v intervalu od nuly do jedné.

def randomList(n):
    s = [0] * n                    # počáteční seznam s nulami
    for i in range(n):             # náhrada nul za náhodné číslo
        s[i] = random.random()
    return s                       # seznam 'n' náhodných čísel
Pomocí této funkce vytvoříme seznam se šesti položkami:

>>> randomList(6)
[0.5199466739572948, 0.452751456638563,
 0.41454566096564627,
 0.7953941766158702, 0.3872848065377861,
 0.9080198286105817]
Předpokládá se, že náhodná čísla, generovaná systémovou funkcí random jsou rovnoměrně rozdělena, to znamená, že výskyt každé hodnoty má (limitně) stejnou pravděpodobnost.

Rozdělíme-li celý interval možných náhodných hodnot do stejně velikých úseků, a spočítáme-li výskyt náhodných hodnot v jednotlivých úsecích, měl by tento výskyt být všude přibližně stejný.

Tento předpoklad si můžeme ověřit napsáním programu, který rozdělí hodnoty do úseků a určí počet výskytů v jednotlivých úsecích, neboli jejich četnost.

9.8 Vytvoření úseků
Označíme-li počet úseků jménem numBuckets a vyjdeme ze skutečnosti, že rozpětí hodnot náhodných čísel má interval 0.0 až 1.0, potom velikost jednoho úseku (bucketWidth) určíme jako podíl 1.0 / numBuckets.

K výpočtu mezí jednotlivých úseků použijeme smyčku. Proměnná i smyčky for počítá s rozpětím nula až (numBuckets-1):

bucketWidth = 1.0 / numBuckets
for i in range(numBuckets):
    low = i * bucketWidth
    high = low + bucketWidth
    print(low, "to", high)
Při výpočtu dolní meze jednotlivého úseku (kyblíku) násobíme proměnnou smyčky podílem na jeden kyblík. Horní mez je o bucketWidth vyšší.

Pro numBuckets = 8 například, jsou rozsahy výstupů následující:

0.0 to 0.125
0.125 to 0.25
0.25 to 0.375
0.375 to 0.5
0.5 to 0.625
0.625 to 0.75
0.75 to 0.875
0.875 to 1.0

9.9 Četnost
Chceme procházet vygenerovaným seznamem náhodných čísel a určovat, kolik náhodných čísel (v intervalu od 0.0 do 1.0) zapadne do některého ze stanovených úseků (buckets). Řešení této úlohy si ukážeme ve dvou variantách:

Opakované traverzování seznamem
Vyjedeme z konstrukce ve cvičení 6.19.2:

count = 0
for char in fruit:
    if char == 'a':
        count = count + 1
print(count)
V prvním kroku nahradíme jména char, fruit označením num a list.

V druhém kroku změníme předmět prověřování. Nezajímá nás výskyt písmen ale chceme vědět, zda se hodnota proměnné num (aktuálně prověřované náhodné číslo) nalézá mezi příslušnými hodnotami low a high.

count = 0
for num in list:
    if low < num < high:
        count = count + 1
print(count)
V posledním kroku zapouzdříme upravený kód do funkce zvané inBucket. Jejími parametry bude seznam všech náhodných čísel list a meze úseků low a high.

def inBucket(list, low, high):
    count = 0
    for num in list:
        if low < num < high:
            count = count + 1
    return count
Právě odvozenou funkci použijeme jako pomocnou funkci v dalším výpočtu.

Pro záznam výskytů náhodných čísel v jednotlivých úsecích vytvoříme seznam výskyty - coby vícečetné počítadlo:

numBuckets = 8                       # počet úseků
výskyty = [0] * numBuckets           # počáteční seznam s nulami
bucketWidth = 1.0 / numBuckets       # číselný rozsah jednoho intervalu
list = randomList(n)                 # seznam - viz odst. 9.7
for i in range(numBuckets):          # pro každý kyblík určit:
    low = i * bucketWidth            # dolní mez intervalu
    high = low + bucketWidth         # horní mez intervalu
    výskyty[i] = inBucket(list, low, high)    # viz **
print(výskyty)     # ** náhrada nul počtem příslušných náhodných čísel
K hladkému provedení výše uvedeného skriptu musí mít interpret Pythonu k disposici importovaný modul random a definice funcí randomList a inBucket.
Nejlépe to zajistíme tak, že založíme soubor buckets.py, do něhož vše potřebné vložíme (včetně  import random  na začátku).

Z výše uvedeného skriptu vytvoříme funkci buckets_a(n,b), když vypustíme řádek numBuckets = 8 a provedeme patřičné odsazení následujících řádků. V těle funkce nahradíme název numBuckets parametrem b.
Soubor uložíme a když v interaktivní konzole IDLE provedeme volání count(1000, 8), získáme takovýto seznam s četnostmi výskytů:

[138, 124, 128, 118, 130, 117, 114, 131]
Tato čísla jsou docela blízká číslu 0.125*1000=125 jak jsme si přáli. Generátor pseudonáhodných čísel nám tedy funguje.

Jednorázové řešení
I když nám tento program chodí, mohl by chodit ještě lépe. Pokaždé, když volá funkci inBucket, prochází opakovaně celým seznamem. S větším počtem kyblíků jde o značný počet cyklů.

Lepší by bylo projít seznamem jen jednou a pro každou hodnotu náhodného čísla určit rovnou index úseku (neboli index položky seznamu výskyty), do kterého náhodné číslo i spadá.

Idea výhodnějšího řešení spočívá v tom, že náhodné číslo i násobíme počtem úseků b. Protože náhodná čísla jsou v rozpětí 0.0 až 1.0, je součin i*b v rozpětí 0.0 až b. Zaokrouhlíme-li každý součin na celé číslo ( int (i * b) ), získáme index položky seznamu výskyty, kam posuzovaná hodnota patří - této položce zvětšíme stav počítadla.

Vytvořenou funkci buckets_b(n,b) přidáme do souboru buckets.py.

def buckets_b(n,b):
    výskyty = [0] * b           # akumulátor
    list = randomList(n)        # volání funkce
    for i in list:
        index = int(i * b)      # zaokrouhlení dolů
        výskyty[index] = výskyty[index] + 1
    print(výskyty)
Poznámka: Seznamuu výskytů se říká frekvenční tabulka, jejímž grafickým zobrazením je sloupcový graf, zvaný histogram.


9.12   Matplotlib
Pouze pro zvídavé
V odstavcích 9.8 a 9.9 je popisováno, jak lze rozdělit pole náhodných čísel [0,1) na intervaly (bucketWidth) a určit počet výskytů náhodných čísel v daném intervalu(výskyty).

Tento soubor čísel (frekvenční tabulku) je možné graficky znázornit histogramem, vytvořeným pomocí knihovny Matplotlib.   Uwaga - je to docela velký macek!

python -m pip install -U matplotlib
Podrobný popis práce s tímto nástrojem lze nalézt například zde.


9.13   Glosář
testem podnícený rozvoj (test-driven development, TDD)
Postup při programování, při kterém se dospěje k žádanému cíli přes řadu malých, postupných kroků, jež jsou ověřovány jednotkovými testy.
blok (block)
Skupina po sobě jsoucích příkazů se stejným odsazením.
histogram
Seznam celých čísel, udávajících četnost výskytu nějaké skutečnosti.
vnoření (nesting)
Jedna programová struktura vnořená do druhé, jako je podmíněný příkaz ve větvi jiného podmíněného příkazu.
9.14   Cvičení
Pro následující doctesty vytvořte záhlaví a těla funkcí, které přidají řádek, případně sloupec do zadané matice. Můžete vyzkoušet postup TDD z odstavce 9.3:
def add_row (matrix):
    """
    >>> m = [[0,0], [0,0]]
    >>> add_row(m)
    [[0, 0], [0, 0], [0, 0]]
    >>> n = [[3, 2, 5], [1, 4, 7]]
    >>> add_row(n)
    [[3,2,5], [1,4,7], [0,0,0]]
    >>> n
    [[3,2,5], [1,4,7]]
    """
def add_column (matrix):
    """
    >>> m = [[0,0], [0,0]]
    >>> add_column(m)
    [[0,0,0], [0,0,0]]
    >>> n = [[3,2], [5,1], [4,7]]
    >>> add_column(n)
    [[3,2,0], [5,1,0], [4,7,0]]
    >>> n
    [[3,2], [5,1], [4,7]]
    """
Všimněte si, že poslední doctesty v každé funkci ověřují, že add_row a add_column jsou funkce čisté.

Napište funkci add_matrices(m1, m2), která vrátí novou matici, jež je součtem matic m1 a m2. Sečíst dvě matice znamená sečíst hodnoty odpovídajících členů. Můžete předpokládat, že matice m1 a m2 mají stejnou velikost.
def add_matrices (m1, m2):
    """
    >>> a = [[1,2], [3,4]]
    >>> b = [[2,2], [2,2]]
    >>> add_matrices(a, b)
    [[3,4], [5,6]]
    >>> c = [[8,2], [3,4], [5,7]]
    >>> d = [[3,2], [9,2], [10,12]]
    >>> add_matrices(c, d)
    [[11,4], [12,6], [15,19]]
    >>> c
    [[8,2], [3,4], [5,7]]
    >>> d
    [[3,2], [9,2], [10,12]]
    """
Poslední dva doctesty opět potvrzují, že add_matrices je čistá funkce.
Napište funkci scalar_mult(n, m), která násobí matici m skalárem n. Doplňte tělo funkce a ujistěte se, že projde doctesty.
def scalar_mult (n, m):
    """
    >>> a = [[1,2], [3,4]]
    >>> scalar_mult(3, a)
    [[3, 6], [9, 12]]
    >>> b = [[3,5,7], [1,1,1], [0,2,0], [2,2,3]]
    >>> scalar_mult(10, b)
    [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
    >>> b
    [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
Na základě získané zkušenosti zkuste násobit matici maticí.
def matrix_mult (m1, m2):
    """
    >>> matrix_mult([[1,2], [3,4]], [[5,6], [7,8]])
    [[19, 22], [43, 50]]
    >>> matrix_mult([[1,2,3], [4,5,6]], [[7,8], [9,1], [2,3]])
    [[31, 19], [85, 55]]
    >>> matrix_mult([[7,8], [9,1], [2,3]], [[1,2,3], [4,5,6]])
    [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """


""" Početní operace s maticemi v příkladech 1 až 4 proveďte i prostřednictvím aplikace Numpy.

Pro lepší porozumění booleovským výrazům jsou dobré pravdivostní tabulky. Dva booleovské výrazy jsou logicky rovnocenné tehdy a jen tehdy, mají-li stejné pravdivostní tabulky.
Následující skript vytiskne pravdivostní tabulku pro libovolný booleovský výraz s proměnnou p a q.
expression = input("Zadej booleovský výraz \
                    pro 'p' a 'q' : " )
print(" p    q    %s"   % expression)
delka = len(" p    q    %s"   % expression)
print(delka* "=")

for p in True, False:
    for q in True, False:
        print("%-7s %-7s %-7s" % (p, q, eval(expression)))
Tento skript použijeme pro osvojení booleovských výrazů. Uložte program do souboru bool_table.py, importujte jej do konzoly interpreta a zadejte 'p or q'. Měl byste dostat následující výstup:
  p       q      p or q
------------------------
True    True      True
True    False     True
False   True      True
False   False     False
Nyní, když víme že kód pracuje, zabalíme jej pro lepší použití do funkce (a uložíme do truth_table.py):
def truth_table(expression):
    print(" p    q    %s"   % expression)
    delka = len(" p    q    %s"   % expression)
    print(delka* "=")

    for p in True, False:
        for q in True, False:
            print("%-7s %-7s %-7s" % (p, q, eval(expression)))
Funkci zavoláme z konzoly IDLE:
>>> truth_table ("p or q")

  p       q      p or q
------------------------
True    True      True
True    False     True
False   True      True
False   False     False
Vyzkoušejte si fci truth_table na následujících booleovských výrazech a zapište si pravdivostní tabulky:
  not (p or q)
  p and q
  not (p and q)
  not(p) or not(q)
  not(p) and not(q)
Které výrazy jsou logicky eqvivalentní?

Napište fci is_divisible(num,f), která přijme celá čísla jako argument a podle situace vytiskne "Toto číslo je dělitelné číslem f" nebo "Toto číslo neni dělitelné číslem f".
Uložte ji do souboru isDivisible.py a řešte v IDLE. Výstup může vypadat takto:

>>> is_divisible(20,4)
Toto číslo je dělitelné číslem 4
>>> is_divisible(21,8)
Toto číslo neni dělitelné číslem 8
Při řešení použijete podmínky if ... :, else: a vyberete si jeden z existujících způsobů dělení: normální a/b, celočíselné a//b a dělení se zbytkem (modulo) a%b.


# ================================
miko oddel
# ================================
10. Entice a sety
# ================================

Vytvoření entice
Složené entice
Pojmenované entice
Hromadné přiřazení
Entice jako výstupní hodnoty
Čisté funkce a modifikátory III
Set a frozenset
Funce zip
Aplikace SeqTools
Glosář
Cvičení

10.1 Vytvoření entice
Entice (tuple) je neměnitelný indexovaný seznam hodnot, oddělených čárkou:

>>> tuple = 'a', 'b', 'c', 'd', 'e'
Zápis na pravé straně vyhodnotí interpret jako entici (tuple) a jako takovou ji vrátí:

>>> tuple
('a', 'b', 'c', 'd', 'e')
Při tvorbě entice s jedinou položkou musíme připojit závěrečnou čárku:

>>> t1 = 'a',            lépe t1 =("a",)
>>> t1; type(t1)
('a',)
<class 'tuple'>
Bez čárky by byl výraz 'a' považován překladačem Pythonu za řetězec.

>>> t2 = ('a')
>>> t2; type(t2)
'a'
<class 'str'>
Odhlédneme-li od skladby, jsou operace s enticemi stejné jako operace se seznamy. Indexový operátor vybere položku z entice:

>>> tuple = ('a', 'b', 'c', 'd', 'e')
>>> tuple[0]
'a'
Úsekový operátor vybere rozsah položek:

>>> tuple[1:3]
('b', 'c')
Pokusíme-li se změnit některou z indexem vybraných položek, dostaneme chybové hlášení:

>>> tuple[0] = 'A'
TypeError: 'tuple' object doesn't support item assignment
Neměnitelnost entice znamená, že ji nelze změnit beze změny identity (ID). Pokud nám nevadí změna ID, můžeme entici - jako přiřazenou hodnotu k proměnné, upravit pomocí součtu entic a úsekového operátoru:

>>> tuple = ('A',) + tuple[1:]
>>> tuple
'A', 'b', 'c', 'd', 'e')

>>> ruple = ('a', 'b', 'c', 'd', 'e'); id(ruple)
56396448
>>> ruple = ruple[:2] + ("C",) + ruple[3:]
>>> ruple; id(ruple)
('a', 'b', 'C', 'd', 'e')
63672720

10.2 Složené entice
Pokud entice obsahuje vložený měnitelný element typu list a dict (nikoliv tuple a set), lze tento prvek změnit obvyklým způsobem a kopírovat metodou copy a deepcopy z modulu copy:

>>> import copy
>>> lt = ("a", [2.5, "b"])            # vložený seznam
# id(lt)     --> 60715336
>>> slt = copy.copy(lt)               # závislá kopie
>>> slt[1][1] = "joj";  lt, slt
(('a', [2.5, 'joj']), ('a', [2.5, 'joj']))
# id(lt), id(slt)     --> (60715336, 60715336)

>>> lt = ("a", [2.5, "b"])
# id(lt)     --> 67797224
>>> dlt = copy.deepcopy(lt)           # nezávislá kopie
>>> dlt[1][1] = "hoj";  lt, dlt
(('a', [2.5, 'b']), ('a', [2.5, 'hoj']))
# id(lt), id(dlt)     --> (67797224, 67797384)
Při úpravě vloženého slovníku musíme zadávat nikoliv index, nýbrž klíč:

>>> import copy
>>> dt = ("a", {2: "b"})              # vložený slovník
# id(dt)     --> 54882600
>>> sdt = copy.copy(dt)               # závislá kopie
>>> sdt[1][2] = "číč";  dt, sdt
(('a', {2: 'číč'}), ('a', {2: 'číč'}))
# id(dt), id(sdt)     --> (54882600 54882600)

>>> dt = ("a", {2: "b"})
# id(dt)     --> 58810760)
>>> ddt = copy.deepcopy(dt)           # nezávislá kopie
>>> ddt[1][2] = "rýč";  dt, ddt
>>> (('a', {2: 'b'}), ('a', {2: 'rýč'}))
# id(dt), id(ddt)     --> (58810760 58810920)
Závislou kopii jak prosté, tak složené entice lze rovněž vytvořit úsekovým operátorem [:]:

>>> tup = ('a', 'b', 'c')
>>> rup = tup[:]; rup
('a', 'b', 'c')
>>> id(tup), id(rup)
(46444232, 46444232)

dt = ("a", {2: "b"})
>>> sdt = dt[:]; sdt
('a', {2: 'b'})
>>> id(dt), id(sdt)
(46497384, 46497384)
Vestavěná metoda tpl.copy() pro entice nechodí.


10.3 Pojmenované entice
Pojmenovaná entice (named tuple) je normální entice, opatřená jménem a názvy položek. Prvky entice jsou tedy kromě indexů přístupné také přes slovní označení.
Práce s pojmenovanou enticí připomíná práci s deklarovanou třídou a jejími instancemi - viz Kap.12. Třídou je zde "matriční" entice, vytvořená pomocí importované funkce namedtuple() z modulu collections:

Název_typu = namedtuple('Název_typu', 'výpis polí' [, rename=False] [, defaults=None] [, module=None])
Z takto obecně deklarované entice (třídy) vytvoříme jednotlivé entice (instance) s konkrétními hodnotami příslušných položek. Užitečnost pojmenované entice spočívá v tom, že si nemusíme pamatovat význam jednotlivých polí.

Práci s pojmenovanou enticí si nejlépe ukážeme na konkrétním příkladě, ve kterém si vytvoříme kartotéku se jmény zaměstnanců, jejich obory a platy (převzato ze stránky DaniWeb s laskavým svolením autora):

# ntEmpRec.py

from collections import namedtuple

Vytvoření vzorové entice s určením polí (atributů):

<název_NT> = namedtuple(<název_NT>, <názvy polí>)    jen dva argumenty

EmpRec = namedtuple('EmpRec', 'name department salary')

Vytvoření konkrétních entic    (lze zadat poziční i pojmenované argumenty)

<jméno_pole> = <název_NT>      (hodnoty jednotlivých atributů)

bob = EmpRec('Bob Zimmer', 'finance', salary = 77123)
tim = EmpRec('Tim Bauer', 'shipping', 34231)

Jiný způsob s použitím seznamu a metody _make:

fred_list = ['Fred Flint', 'purchasing', 42350]
fred = EmpRec._make(fred_list)
Jiný způsob s použitím slovníku a dvojhvězdičkového operátoru:

fred_dict = {'name': 'Fred Flint', 'department': 'purchasing', 'salary': 42350}
fred = EmpRec(**fred_dict)
--> EmpRec{'name': 'Fred Flint', 'department': 'purchasing', 'salary': 42350}

Vytvoření entice z existující entice metodou _replace:

john = fred._replace(name='John Ward', salary=49200)

Vytvoření implicitní entice pro dělníky s hodinovou mzdou

default = EmpRec('addname', 'manufacturing', 26000)

a její aplikace pro tvorbu konkretních entic

mike = default._replace(name='Mike Holz')
gary = default._replace(name='Gary Wood')
carl = default._replace(name='Carl Boor')

Převedení entice na slovník metodou _asdict():

print(bob._asdict())

Výpis polí entice přes název entice či vzorové entice:

print(bob._fields)
print(EmpRec._fields)
=== RESTART: F:\Codetest\HowTo\ch-10\in-text\ntEmpRec.py ===
{'name': 'Bob Zimmer', 'department': 'finance', 'salary': 77123}
('name', 'department', 'salary')
('name', 'department', 'salary')

Přístup k polím přes jméno entice a atributu
>>> print(bob.name, bob.salary)
Bob Zimmer 77123

Přístup k polím přes jméno entice a index atributu
>>> print(tim[0], tim[2])
Tim Bauer 34231
Vytvoření seznamu pojmenovaných entic:

# ntEmpRec.py selektivně upravené
...
print('-'*40)
emp_list = [bob, fred, tim, john, mike, gary, carl]
for emp in emp_list:
    print( "%-15s works in %s" % (emp.name, emp.department) )
print('-'*40)
== RESTART: F:/Codetest/HowTo/ch-10/in-text/listEmpRec.py ==
----------------------------------------
Bob Zimmer      works in finance
Fred Flint      works in purchasing
Tim Bauer       works in shipping
John Ward       works in purchasing
Mike Holz       works in manufacturing
Gary Wood       works in manufacturing
Carl Boor       works in manufacturing
----------------------------------------
Pro výpis polí používá Python interně metodu split():

>>> "name department salary".split()
['name', 'department', 'salary']
Objekt EmpRec lze tedy alternativně deklarovat takto:

>>> EmpRec = namedtuple('EmpRec', ['name', 'department', 'salary'])
Případně:
>>> EmpRec = namedtuple('EmpRec', ('name department salary'))
>>> type(EmpRec)
<class 'type'>                    # vida, ona je to třída
Podporované metody
Kromě prezentovaných metod _replace(), _make(), _asdict(), _fields podporuje named tuple stejné metody jako regulérní typ tuple - min(), max(), len(), in, not in, concatenation, index, slice, atd.

Aktuálně platné parametry funkce namedtuple - rename, defaults a module viz namedtuple() v anglické dokumentaci.


10.4 Hromadné přiřazení
Hromadné přiřazení (multiple assignment) umožňuje přiřadit několika proměnným příslušné hodnoty na jediném řádku.

Víme již, že entici bez závorek akceptuje interpret jako entici se závorkami:

>>> x, y = 10, 20        # --> (x, y) = (10, 20)
>>> x, y
(10, 20)
Popsaný způsob přiřazení lze použít nejen u entic ale i u dalších 'iteráblů' - slovníků [], setů {} a řetězců " ".

>>> a, b = [12, 22]
>>> c, d = {14, 24}
>>> e, f = "Hi"
>>> a,b, c,d, e,f
(12, 22, 24, 14, 'H', 'i')
Rozbalení entice použijeme výhodně při záměně přiřazení:

>>> x, y = 10, 20
>>> x, y = y, x
>>> x, y
(20, 10)
Při rozbalování entice lze použít pomocnou proměnnou:

>>> ent = "m", 2, False
>>> x,y,z = ent
>>> z,y,x
(False, 2, 'm')
Počet prvků po obou stranách přiřazení musí být shodný.

10.5 Entice jako výstupní hodnoty
Funkce mohou vracet entici jako výstupní hodnotu. Můžeme například napsat funkci, která zamění dva parametry:

def swap(x, y):
    return y, x
Při používání tété funkce je zapotřebí jisté ostražitosti:

>>> a, b = 10,5
>>> swap(a, b)
(5,10)                 # dostali jsme co jsme chtěli
>>> a,b
(10,5)                 # vstupní hodnoty jsme ale nezměnili
>>> a,b = swap(a, b)   # musíme o to výslovně požádat
>>> a,b
(5,10)
Enticové přiřazení uvnitř funce swap se v prostoru __main__ neprojeví.

Tato funkce případně neprovede to, co jsme si přáli. To je příklad sémantické (významové) chyby.

Přehlednější ukázkou použití entice pro výstupní hodnoty funkce je tento příklad:

from math import pi
def kruh(r):
    c = 2 * pi * r          # obvod kruhu
    a = pi * r * r          # plocha kruhu
    return (r, c, a)

10.6 Čisté funkce a modifikátory III
V kapitole 3.5 a 3.7 jsme si povídali o čistých funkcích a modifikátorech v souvislosti se seznamy. Pro entice modifikátory psát nemůžeme, protože entice jsou samy o sobě neměnitelné.

Zde máme modifikátor, který vloží novou hodnotu val do středu seznamu lst. Text kódu si uložíme do souboru pureTriTools.py a spustíme si ho v IDLE, abychom viděli, jak chodí:

# pureTriTools.py

def insert_in_middle_lst(val, lst):
    middle = int(len(lst)/2)
    lst[middle:middle] = [val]
>>> my_list = ['a', 'b', 'd', 'e']
>>> insert_in_middle_lst('c', my_list)
>>> my_list
['a', 'b', 'c', 'd', 'e']
Zkusíme-li to s enticí, dostaneme chybu. Problém je ten, že entice jsou neměnitelné a nepodporují úsekové přiřazení. Jednoduchým řešením je udělat z insert_in_middle_lst čistou funkci:

def insert_in_middle_tup(val, tup):
    middle = int(len(tup)/2)
    return tup[:middle] + (val,) + tup[middle:]
Tato verze nyní chodí pro entice, ne však pro seznamy a řetězce.

>>> my_tuple = ('a', 'b', 'd', 'e')
>>> insert_in_middle_tup('c', my_tuple)
('a', 'b', 'c', 'd', 'e')
Chceme-li verzi pro všechny sekvenční typy, potřebujeme zapouzdřit naši hodnotu do správného sekvenčního typu. Malá pomocná funkce vykoná div:

def encapsulate(val, seq):
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)
Nyní můžeme napsat insert_in_middle tak, aby pracovala s každým vestavěným typem sekvence:

def insert_in_middle(val, seq):
    middle = int(len(seq)/2)
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]
Poslední dvě verze insert_in_middle jsou čisté funkce. Nemají žádné postranní účinky. Přidáme-li encapsulate a poslední verzi insert_in_middle do modulu pureTriTools.py, můžeme to vyzkoušet:

>>> from pureTriTools import *

>>> my_string = 'abde'
>>> insert_in_middle('c', my_string)
'abcde'

>>> my_list = ['a', 'b', 'd', 'e']
>>> insert_in_middle('c', my_list)
['a', 'b', 'c', 'd', 'e']

>>> my_tuple = ('a', 'b', 'd', 'e')
>>> insert_in_middle('c', my_tuple)
('a', 'b', 'c', 'd', 'e')

>>> my_string
'abde'
Hodnoty my_string, my_list, a my_tuple se nezměnily.


10.7 Set a frozenset
Set (množina) je neuspořádaná měnitelná kolekce odlišných prvků, frozenset je neměnitelná kolekce odlišných prvků. Používají se při testování "členství" a při eliminaci duplikátních zápisů.

Kolekce set a frozenset podporují množinové operace sjednocení (union), průnik (intersection), rozdíl (difference) a doplněk (symmetric_difference), funkci len(s) a idiomy x in s, x not in s.

Set vytvoříme buď výčtem nebo pomocí funkce set(), frozenset vytvoříme pouze funkcí frozenset(). Obě funkce přijímají pouze jeden argument, jímž může být seznam, řetězec, entice, částečně i slovník. Pozice jednotlivých prvků není indexována.

>>> basket = {'apple','orange','apple','pear','orange','banana'}
>>> basket
{'orange', 'apple', 'banana', 'pear'}      # žádné duplikáty!
>>> tup = (1,2,3,"alpha",2)
>>> st = set(tup)
>>> st
{1, 2, 3, 'alpha'}                         # žádné duplikáty!
>>> fr = frozenset('alcatraz')
>>> fr
frozenset({'a', 'c', 'l', 'r', 't', 'z'})  # žádné duplikáty!
Použijeme-li jako argument pro funkce set a frozenset slovník, použijí se pouze hodnoty jeho klíčů:

>>> dic = {"a": 1, "b": 2, "c": 3}
>>> set_dic = set(dic)
>>> set_dic
{'b', 'c', 'a'}
Set i frozenset mají definovanou částečně společnou řadu metod:

set_meth = add, clear, copy, difference, difference_update,
discard, intersection, intersection_update, isdisjoint, issubset,
issuperset, pop, remove, symmetric_difference,  union, update,
symmetric_difference_update

frozenset_meth = copy, difference, intersection, isdisjoint,
issubset, issuperset, symmetric_difference,  union
Objekt typu set nepodporuje změnu položky. Obsah setu lze nicméně měnit metodami add, clear, discard, pop, remove a update. Set i frozenset jsou rovněž vybaveny funkcí next(~) a metodou .__next__(), jsou to tedy iterábly.

Ukážeme si některé operace na setech:

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a, b                 # zápis entice
({'a', 'c', 'b', 'r', 'd'}, {'a', 'c', 'z', 'm', 'l'})
>>> a - b                # rozdíl
{'r', 'd', 'b'}          # b-a --> {'z', 'm', 'l'}
>>> a | b                # sjednocení
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                # průnik
{'a', 'c'}
>>> a ^ b                # doplněk
{'r', 'd', 'b', 'm', 'z', 'l'}
Stejně jako pro seznam lze i pro set definovat komprehenci setu:

>>> s = {v for v in "ABCDABCD" if v not in "CB"}
>>> s
>>> {'A', 'D'}
Zápisy (), [], {} označují práznou entici, seznam a slovník; zápisy set() a frozenset() (nikoliv {}) označují prázdný set a frozenset.


10.8 Funkce zip
Funkce zip(*iterables) přijímá jednu či více sekvencí a kombinuje jejich položky do řady entic uvnitř interního iterátorového objektu.
Tento výsledný seznam či entice je iterátorem, jenž je po použití prázdný a před případným opakovaným použitím se musí opětovně deklarovat.

>>> izip = zip([1, 2, 3, 4], "postel")    #  sekvencí může být i více
>>> izip
<zip object at 0x000002194D5E0B40>        # interní iterátorový objekt

>>> list(izip)                                #  použití iterátoru
[(1, 'p'), (2, 'o'), (3, 's'), (4, 't')]
>>> set(izip)                                 #  iterátor je prázdný!
set()
>>> set(zip([1, 2, 3, 4], "postel"))          #  použití s deklarací
{(4, 't'), (3, 's'), (2, 'o'), (1, 'p')}
>>> tuple(zip([1, 2, 3, 4], "postel"))        #  použití s deklarací
((1, 'p'), (2, 'o'), (3, 's'), (4, 't'))
>>> dict(zip([1, 2, 3, 4], "postel"))         #  použití s deklarací
{1: 'p', 2: 'o', 3: 's', 4: 't'}
Počet entic ve výsledném iterátoru je dán délkou nejkratšího argumentu funkce zip. Zazipované sekvence lze opět odzipovat:

nl = [1, 2, 3]
sl = ['one', 'two']
nt = ('ONE', 'TWO', 'THREE', 'FOUR')

izip = zip(nl, sl, nt)
result_list = (list(izip))
print("result_list =",result_list)

nl, sl, nt = zip(*result_list)                  #  sběrný parametr

print("nl =",nl, "sl =",sl, "nt =",nt)

========== RESTART: F:/Codetest/python/zip_test.py =========
result_list = [(1, 'one', 'ONE'), (2, 'two', 'TWO')]
nl = (1, 2) sl = ('one', 'two') nt = ('ONE', 'TWO')
Proměnné   nl, sl, nt  změnily trvale svou hodnotu.


10.9 Aplikace SeqTools
SeqTools je sada knihoven pro manipulaci se sekvenčními daty typu list, tuple, range, bytes a bytearray . Velice pěkné seznámení s tímto nástrojem nalezneme na stránce SeqTools.
Zde se seznámíme s řadou metod, které lze s příslušným importem využívat.

Předtím je nutné si tento nástroj instalovat:

pip install seqtools          Jak prosté, milý Watsone!
Oprašte svou angličtinu a naučte se pracovat s nástrojem SeqTools.


10.10 Glosář
entice (tuple)
Typ s uspořádanými položkami jako u seznamu, zde však jsou položky neměnitelné. Entice mohou být použity všude tam, kde je požadován neměnitelný typ, jako v klíči u slovníku.
enticové přiřazení (tuple assignment)
Přiřazení všem elementům entice jediným příkazem k přiřazení. Enticové přiřazení se realizuje paralelně, takže je vhodné pro záměnu hodnot.
set
Set je neuspořádaná měnitelná kolekce nestejných prvků s neměnitelnou hodnou.

10.11 Cvičení
Generujte náhodné číslo mezi low a high.
Generujte náhodné celé číslo mezi low a high včetně.
Předpokládá se, že čísla, generovaná systémovou funkcí random jsou rovnoměrně rozdělena, to znamená, že výskyt každé hodnoty má stejnou pravděpodobnost.
Zapište upravenou funkci countB1(n,b) z konce odstavce 9.9 do souboru histogram.py a vyzkoušejte volání pro n = 2000, 4000, 8000, b = 8. Ověřte, zda četnosti spějí k rovnoměrnénu výskytu.
Do stejného souboru připište upravenou funkci countB2(n,b) z konce odstavce 9.10. Volejte ji pro stejné hodnoty jako v předchozí úloze.
Vytvořte soubor lists_one.py (kap. 8), vložte do něj následující doctesty a doplňte vhodnými definicemi funkcí:
def make_empty(seq):
    """
    >>> make_empty([1, 2, 3, 4])
    []
    >>> make_empty(('a', 'b', 'c'))
    ()
    >>> make_empty("No, not me!")
    ''
    """

def insert_at_end(val, seq):
    """
    >>> insert_at_end(5, [1, 3, 4, 6])
    [1, 3, 4, 6, 5]
    >>> insert_at_end('x', 'abc')
    'abcx'
    >>> insert_at_end(5, (1, 3, 4, 6))
    (1, 3, 4, 6, 5)
    """

def insert_in_front(val, seq):
    """
    >>> insert_in_front(5, [1, 3, 4, 6])
    [5, 1, 3, 4, 6]
    >>> insert_in_front(5, (1, 3, 4, 6))
    (5, 1, 3, 4, 6)
    >>> insert_in_front('x', 'abc')
    'xabc'
    """

def index_of(val, seq, start=0):
    """
    >>> index_of(9, [1, 7, 11, 9, 10])
    3
    >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
    3
    >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
    6
    >>> index_of('y', 'happy birthday')
    4
    >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
    1
    >>> index_of(5, [2, 3, 4])
    -1
    >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
    -1
    """

def remove_at(index, seq):
    """
    >>> remove_at(3, [1, 7, 11, 9, 10])
    [1, 7, 11, 10]
    >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
    (1, 4, 6, 7, 0, 3, 5)
    >>> remove_at(2, "Yomrktown")
    'Yorktown'
    """

def remove_val(val, seq):
    """
    >>> remove_val(11, [1, 7, 11, 9, 10])
    [1, 7, 9, 10]
    >>> remove_val(15, (1, 15, 11, 4, 9))
    (1, 11, 4, 9)
    >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
    ('who', 'when', 'where', 'why', 'how')
    """

def remove_all(val, seq):
    """
    >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
    [1, 7, 9, 10, 2]
    >>> remove_all('i', 'Mississippi')
    'Msssspp'
    """

def count(val, seq):
    """
    >>> count(5, (1, 5, 3, 7, 5, 8, 5))
    3
    >>> count('s', 'Mississippi')
    4
    >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
    2
    """

def reverse(seq):
    """
    >>> reverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse(('shoe', 'my', 'buckle', 2, 1))
    (1, 2, 'buckle', 'my', 'shoe')
    >>> reverse('Python')
    'nohtyP'
    """

def sort_sequence(seq):
    """
    >>> sort_sequence([3, 4, 6, 7, 8, 2])
    [2, 3, 4, 6, 7, 8]
    >>> sort_sequence((3, 4, 6, 7, 8, 2))
    (2, 3, 4, 6, 7, 8)
    >>> sort_sequence("nothappy")
    'ahnoppty'
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
Odjíždíte na báječnou dovolenou ve středu, to je ve 3. dnu v týdnu. Vrátíte se po 137 nocích. Napište program, který se zeptá na pořadové číslo dne vašeho odjezdu, délku pobytu a vrátí vám název dne, ve kterém se vrátíte. Bude to neděle?
Použijete vstup z klávesnice, operátor modulo, den návratu vyberete indexem.
Případně můžete napsat funkci 'návrat(odjezd, délka)'.



# ================================
miko oddel
# ================================
11. Slovníky
# ================================

Slovníkové operace
Slovníkové metody
Sloučení slovníků
Komprehence slovníku
Alias a kopírování
Řídké matice
Switch case
Výskyty znaků
Výskyty slov
Glosář
Cvičení
Dosud poznané složené datové typy – řetězce, seznamy a entice – jsou sekvence, které používají celá čísla jako indexy pro přístup k jednotlivým položkám.

Slovníky, řazené mezi kolekce, používají jiný systém pro přístup k položkám. Za jednu položku je považována dvojice klíč:hodnota. Klíčem může být pouze neměnitelný datový typ, hodnotou libovolný datový typ.

Jako příklad vytvoříme slovník pro překlad anglických slov do španělštiny. Klíči u tohoto slovníku budou řetězce.

Začneme tak, že vytvoříme prázdný slovník, do kterého přidáme párové položky. Prázdný slovník se označuje {}:

>>> eng2sp = {}
>>> eng2sp['one'] = 'uno'
>>> eng2sp['two'] = 'dos'
>>> eng2sp
{'one': 'uno', 'two': 'dos'}
První přiřazení vytvoří prázdný slovník s názvem eng2sp, další přiřazení přidávají nové párové položky.
Párové položky jsou oddělené čárkami. Každý pár obsahuje klíč a hodnotu, oddělenou dvojtečkou.

Jiným způsobem vytvoříme slovník tak, že přímo zadáme seznam párů klíč-hodnota:

>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
Hodnoty ve slovníku jsou přístupné prostřednictvím klíčů, nikoliv indexů.

Takto použijeme klíče k vyhledání odpovídající hodnoty:

>>> eng2sp['two']
'dos'
Klíčový operátor použijeme také pro přidání nové dvojice na konec slovníku:

>>> eng2sp['four'] = "quatro"
>>> eng2sp
{'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'quatro'}

11.1 Slovníkové operace
Příkaz del odstraní dvojici klíč-hodnota ze slovníku. Následující slovník na příklad obsahuje jména různého druhu ovoce a jeho množství na skladě:

>>> inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}
>>> inventory
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
Když někdo skoupí všechny hrušky, můžeme tento vstup ze slovníku vyjmout:

>>> del inventory['pears']
>>> inventory
{'apples': 430, 'bananas': 312, 'oranges': 525}
Nebo očekáváme-li, že hrušky zase budou, můžeme pouze změnit hodnotu spojenou s hruškami:

>>> inventory['pears'] = 0
>>> inventory
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 0}
U slovníku můžeme také použít funkci len, která vrací počet dvojic klíč-hodnota:

>>> len(inventory)
4

11.2 Slovníkové metody
Slovníky mají řadu užitečných vestavěných metod, jejichž seznam získáme známou funkcí dir():

>>> dir(dict)
[__...__, 'clear', 'copy', 'fromkeys', 'get', 'items',
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
Metoda get přijme klíč a vrátí párovou hodnotu:

>>> car = {"brand": "Ford", "model": "Mustang","year": 1964}
>>> x = car.get("model")
Mustang
Metoda keys přijme slovník a vrátí seznam jeho klíčů:

>>> eng2sp.keys()
dict_keys(['one', 'two', 'three',)
Tato forma tečkové notace uvádí jméno objektu eng2sp a jméno aplikované metody keys. Prázdné závorky naznačují, že tato metoda nepřijímá žádné parametry.

Volání metody se nazývá invokace; v tomto případě bychom řekli, že invokujeme metodu keys pro objekt eng2sp.

Metoda values je podobná; vrací seznam hodnot ve slovníku:

>>> eng2sp.values()
dict_values(['uno', 'dos' 'tres'])
Metoda items vrací obojí formou seznamu entic:

>>> eng2sp.items()
dict_items([('one', 'uno'), ('two', 'dos'), ('three', 'tres')])
Syntaxe poskytuje užitečnou informaci o typech. Hranaté závorky naznačují, že jde o seznam. Oblé závorky naznačují, že položkami seznamu jsou entice.

Přítomnost klíče ve slovníku lze ověřit idiomem s klíčovým slovem in:

>>> "one" in eng2sp
True
>>> "deux" in eng2sp
False

11.3 Sloučení slovníků
Verze Python 3.9.0 přináší dva nové operátory pro sloučení slovníků, sjednocení (dict union) d|e   a rozšířené přiřazení (augmented assignemt) d |= e.

Sjednocení | sloučí obsah obou operandů (zde slovníků). Nachází-li se stejný klíč v obou operandech, pro sloučení se vybere ten z pravého operandu - viz případ d | e a e | d. Tato operace není komutativní (d | e != e | d):

>>> d = {'spam': 1, 'eggs': 2, 'cheese': 3}
>>> e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
>>> d | e
{'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
>>> e | d
{'cheese': 3, 'aardvark': 'Ethel', 'spam': 1, 'eggs': 2}
Rozšířené přiřazení provede přiřazení se sjednocením:

>>> d |= e
>>> d
{'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
# Podivný je tento výsledek:
>>> e
{'cheese': 'cheddar', 'aardvark': 'Ethel'}
Rozšířené přiřazení lze použít k rozšíření slovníku:

>>> d |= [('spam', 999)]
>>> d
{'spam': 999, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}

11.4 Komprehence slovníku
Komprehence slovníku se příliš neliší od komprehence seznamu. Výstupem z komprehence slovníku je slovník, vytvořený aplikací zadaného výrazu pro každý element iteráblu. Schematická skladba je tato:

{key: value for (key [, value]) in iterable}
Iteráblem zde může dle okolností být objekt typu string, list, tuple, range, bytes, bytearray, dict, set, frozentset.

>>> dct_range = {x: x**2 for x in range(5)}
>>> print(dct_range)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Totéž pomocí mrožího operátoru:
>>> print(dct_range := {x: x**2 for x in range(5)})
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Při komprehenci slovníku můžeme použít i funkci zip():

>>> keys = ['a', 'b', 'c']
>>> vals = [1, 2, 3]
>>> print(dict_compr_zip := {keys:vals \
...     for (keys,vals) in zip(keys, vals)})
{'a': 1, 'b': 2, 'c': 3}
>>> dict_compr_zip         vytvořenou proměnnou lze nezávisle použít
{'a': 1, 'b': 2, 'c': 3}

11.5 Alias a kopírování
Protože jsou slovníky měnitelné, musíme si dát pozor na aliasování. Kdykoliv dvě proměnné odkazují ke stejnému objektu, jeho změna prostřednictvím jedné proměnné je sdílena i druhou proměnnou.

Chceme-li měnit slovník a přitom si zachovat kopii originálu, použijeme metodu copy. Například, oppos je slovník, který obsahuje dvojice protikladů:

>>> oppos = {'up': 'down', 'right': 'wrong', 'true': 'false'}
>>> alias = oppos                  id(alias) == id(oppos)
>>> kopie = oppos.copy()           id(kopie) != id(oppos)
Proměnné alias a oppos odkazují na stejný objekt, proměnná kopie odkazuje na nezávislou kopii téhož slovníku. Upravíme-li alias, změní se i oppos:

>>> alias['right'] = 'left'
>>> oppos['right']
'left'
Když naproti tomu upravíme kopie, tak se oppos nezmění:

>>> kopie['right'] = 'privilege'
>>> oppos['right']
'left'

11.6 Řídké matice
V odstavci 9.3 jsme použili seznam seznamů k prezentaci matice. To je dobrý způsob pro matice s převážně nenulovými hodnotami, uvažme však řídkou matici jako je tato:



Vyjádření matice prostřednictvím seznamu obsahuje množství nul:

matrix = [ [0,0,0,1,0],
           [0,0,0,0,0],
           [0,2,0,0,0],
           [0,0,0,0,0],
           [0,0,0,3,0] ]
Alternativou je použití slovníku. Jako klíče můžeme použít entice, obsahující pořadová čísla řádků a sloupců (pořadí začíná nulou jako u indexů). Zde je slovníkové vyjádření téže matice:

>>> matrix = {(0,3): 1, (2,1): 2, (4,3): 3}
Potřebujeme jenom tři dvojice klíč: hodnota pro tři nenulové prvky matice. Každý klíč je entice a každá hodnota je celé číslo.

Prvky matice jsou přístupné pomocí operátoru [ ]:

>>> matrix[0,3]
1
Všimněme si, že vyjádření matice slovníkem má jinou skladbu než vyjádření matice vnořenými seznamy. Místo dvou celočíselných indexů používáme jenom jeden, jímž je entice z celých čísel.

Je zde však jeden problém. Pokusíme-li se ukázat na nulový prvek matice, dostaneme chybu, protože ve slovníku takový klíč uvedený nemáme:

>>> matrix[1,3]
keyerror: (1, 3)
Tento problém řeší metoda get:

>>> matrix.get((0,3), 0)
1
Prvním argumentem je klíč, druhým argumentem je hodnota, kterou má funkce get vrátit, nebude-li zadávaný klíč ve slovníku:

>>> matrix.get((1,3), 0)
0
Metoda get rozhodně zlepšuje přístup k prvkům řídké matice.


11.7 Switch case
Výběrovou proceduru switch case či dispatch lze v Pythonu vytvořit pomocí slovníku. Místo sekvence podmínek if.., elif.., else pro volání existujících funkcí (viz kap. 4.2.4) lze deklarovat slovník, který přiřadí zvolené klíče (lze také použít číslice) k již definovaným funkcím a protože funkce v Pythonu jsou objekty prvního řádu, lze si jednotlivé funkce volat jednoduchým příkazem:

def func_a(): print("fce-a")
def func_b(): print("fce-b")
def func_c(): print("fce-c")

oslík = {"a": func_a, "b": func_b, "c": func_c}

def print_f(value):              # Včetně částečného ošetření výjimek
    oslík.get(value, lambda: print("Neplatné!"))()
Výběr funkce provedeme voláním funkce print_f(value) nebo (protože máme výběrový slovník uveden samostatně) zadáním vybraného klíče slovníku:

===== RESTART: F:\Codetest\HowTo\ch-09\a9a_dispatch.py =====

>>> print_f("b")
fce-b
>>> print_f(5)
Neplatné

>>> oslík["c"]()             # Kulaté závorky dotvářejí volání funkce.
fce-c
Volané funkce mohou být také deklarovány jako vložené funkce lambda:

def kalkul(operátor, x, y):
    cases = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b, }
# Deklarované případy:
    if operátor in cases.keys():
        return cases[operátor](x, y)
# Částečné ošetření výjimek
    else:
        return cases.get(operátor, "Nenalezeno!")
============ RESTART: F:\Codetest\HowTo\tremp.py ===========

>>> kalkul('/', 5, 2)
2.5
>>> kalkul(print, 5, 2)               # Viz poznámka
Nenalezeno!
>>> calcul(^, 5, 3)
SyntaxError: invalid syntax
Poznámka: Zadáme-li jakoukoli pro Python známou hodnotu (mimo deklarované argumenty +,-,*,/), dozvíme se, že "Nenalezeno". V případě zadání v daném kontextu neznámé hodnoty dojde k chybovému hlášení.

Variace: Funkce lambda lze zajisté nahradit funkcemi pro operace +, -, *, a /. Příslušný výraz se nahradí voláním odpovídající funkce, například:

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

def kalk(operátor, x, y):
    cases = {"+": add, "-": sub, "*": mul, "/": div}
    return cases[operátor](x, y)
Simulaci přepínače lze také vytvořit prostřednictvím třídy.


11.8   Výskyty znaků
V kapitole 6.19, cvičení 2 a 3 jsme počítali výskyt zadaného znaku v zadaném řetězci a to pomocí smyčky s počítadlem, případně přímo prostřednictvím metody 'count'.
Také jsme v kap.9.8 počítali výskyty náhodných čísel v jednolivých úsecích rozpětí 0.0 až 1.0 jako potvrzení skutečnosti, že funkce 'random' modulu 'random' generuje pseudonáhodná čísla.
Použití počítadla s UCP
V následujícím komentovaném programu countLetters.py spočítáme výskyt znaků (písmen) v zadaném textu (Alice in Wonderland) s použitím seznamu 'counts' coby mnohočetného počítadla:

# countLetters.py

# Ošetření tisknutelných (chr(i)) i netisknutelných znaků:

def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)           # vrací tisknutelný znak.

Tato funkce bude opakovaně použita v následné smyčce.
Argument 'i' je UCP (Unicode Code Point) zkoumaného znaku.

# Načtení textu ze souboru do paměti interpreta:

inpath = '../files_txt/alice_wonderland.txt'  # cesta k souboru
infile = open(inpath, encoding="utf-8")
text = infile.read()          # 'text' má formát řetězce
infile.close()

Pro anglický text (kódování ASCII) lze zadat délku seznamu
counts = 127 * [0],
pro český text (UTF-8) je nutné zadat counts = 383 * [0]

Případně pokud umíme určit max UCP jako zde:
>>> text = "abcde\n efgh"
>>> ord(max(text)) --> 104 --> counts = 105 * [0]
můžeme použít seznam kratší.

Položky seznamu 'counts' jsou receptory výskytů jednotlivých
písmen. Zjištěné hodnoty UCP slouží jako indexy seznamu

# Načtení výskytů do seznamu 'counts':

counts = 127 * [0]                # max UCP pro ASCII = 126
for letter in text:
    counts[ord(letter)] += 1      # přičítá výskyty znaků
     # ord(letter) je aktuální index seznamu 'counts'

# Strukturovaný zápis výskytů do souboru 'letter_counts.dat':

outpath = '../files_dat/letter_counts.dat'   # deklarace cesty
outfile = open(outpath, 'w')      # otevření/vytvoření souboru

# formátované záhlaví souboru:
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

# formátovaný obsah pod záhlavím:
for i in range(len(counts)):           # len(counts) = 126+1
    if counts[i]:                        # if counts[i] != 0
        outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()         # povinné zavření otevřeného souboru

Funkce 'range' v proceduře 'range(len(counts))'
je důvodem ke zvýšení délky seznmu 'count' o 1.

# Toto oznámení se vytiskne v konzole interpreta IDLE:

print("Frekvenční tabulka je v souboru ", outpath)
print("Délka souboru 'counts' a počet znaků: ",
                           len(counts), len(text))

# Frekvenční tabulku si prohlédneme v souboru 'letter_counts.dat'.
Spusťte si tento program v IDLE a prohlédněte si generovaný výstupní soubor v textovém editoru.

Použití slovníku
Pomocí slovníku vytvoříme seznam výskytů znaků elegantním způsobem:

>>> letter_counts = {}
>>> for letter in "Mississippi":
...     letter_counts[letter] = letter_counts.get (letter, 0) + 1
...
>>> letter_counts
{'M': 1, 'i': 4, 's': 4, 'p': 2}
Začínáme prázdným slovníkem. Pro každé písmeno v řetězci zvětšíme aktuální četnost o 1. Na konci procesu máme slovník obsahující dvojice písmen a jejich četností.

Bylo by ještě působivější, kdybychom výskyt písmen uspořádali podle abecedy. Můžeme to udělat pomocí univerzální funkce sorted(). Tuto funkci lze použít pro seznamy, řetězce, entice, sety i slovníky:

>>> sorted(letter_counts)
['M', 'i', 'p', 's']
>>> sorted(letter_counts.items())
[('M', 1), ('i', 4), ('p', 2), ('s', 4)]
Proč je M před i? Vzpomeňte si na funkci ord():

>>> ord("M"), ord("i")
(77, 105)

11.9   Výskyty slov
Výskyt zadaného slova ve vstupním řetězci určíme jednoduše metodou count:

text = "apple mango apple orange orange apple guava\
        mango mango"
def word_count(text, word)
    print(word + " " + str(text.count(word)))
>>> word_count(text, "mango")
mango 3
Nejjednodušší způsob určení výskytu slov v textu je metodou add a count poté, co jsme si připravili prázdný kolektor typu set a vstupní řetězec konvertovali na seznam:

text = "Woodchuck, how much wood would a woodchuck \
        chuck if a woodchuck could chuck wood ?"

sett = set()              # prázdný kolektor typu 'set'
lstt = text.split()       # konverze stringu na list

for i in lstt:
    sett.add((i, lstt.count(i)))  # 'add' přijímá 1 arg.
S výstupem coby slovník:

>>> print(dict(sett))      # konverze setu na slovník
{'a': 2, 'would': 1, 'how': 1, 'much': 1,
'could': 1, 'chuck': 2, 'Woodchuck,': 1,
'wood': 2, 'woodchuck': 2, '?': 1, 'if': 1}
Případně coby seznam:

>>> print(list(sett))      # konverze setu na seznam
[('?', 1), ('chuck', 2), ('woodchuck', 2), ('would', 1),
('Woodchuck,', 1), ('how', 1), ('wood', 2), ('could', 1),
('much', 1), ('a', 2), ('if', 1)]

11.10 Glosář
slovník (dictionary)
Kolekce dvojic klíč-hodnota, kde klíče ukazují na hodnotu (mapují hodnotu). Klíčem může být jakýkoliv neměnitelný typ, hodnoty mohou být libovolného typu.
dvojice klíč-hodnota (key-value pair)
Párová položka ve slovníku.
invokace (invocation)
Volání metody či funkce
náznak (hint)
Spočítaná a dočasně uložená hodnota, nahrazující zbytečně opakovaný výpočet.
přetečení (overflow)
Číselný výsledek příliš veliký na to, aby mohl být reprezentován číselným formátem.
11.11 Cvičení
Napište funkci, která přijme řetězec ("Až na severní pól šel bych rád") a vrátí frekvenční tabulku, coby slovník s uspořádanými klíči:
def letter_counts(retiazka):
    ...
Výstup pro "Mississippi" má tvar:

>>> letter_counts("Mississippi")
{'M': 1, 'i': 4, 'p': 2, 's': 4}
Pokuste se přeformulovat předchozí úlohu tak aby výstupní frekvenční tabulka pro "Mississippi" měla formát:

M   1
i   4
s   4
p   2
Pro formulaci výstupu můžete použít postup, použitý v kap. 11.8. Nezapomeňte si prohlédnout generovaný výstupní soubor

Uveďte odezvu interpreta v sedmi následujících případech v jedné souvislé seanci:
>>> d = {"apples":15, "bananas":35, "grapes":12}
>>> d["bananas"]
>>> d["oranges"] = 20
>>> len(d)
>>> "grapes" in d
>>> d["pears"]
>>> d.get("pears", 0)
>>> fruits = d.keys()
>>> sorted(fruits)
>>> del d["apples"]
>>> "apples" in d
Sem přijde vymyslet příklad na slovníkový "dispatch" - odstavec 8.
Doplňte tělo funkce, která upravuje obsah slovníku new_inventory

def add_fruit(inventory, fruit, quantity=0):
    pass

# tyto testy by měly vyjít
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
test('strawberries' in new_inventory, True)
test(new_inventory['strawberries'], 10)
add_fruit(new_inventory, 'strawberries', 25)
test(new_inventory['strawberries'] , 35)
Soubor unsorted_fruits.txt obsahuje seznam 26 druhů ovoce, přičemž každé jméno začíná jiným písmenem abecedy.
Napište program sort_fruits.py, který načte ovoce z unsorted_fruits.txt a zapíše je v abecedním pořádku do sorted_fruits.txt.

Napište program alice_words.py, který vytvoří textový soubor alice_words.txt obsahující abecedně uspořádaný výpis slov z alice_in_wonderland.txt spolu s počtem výskytů každého slova. Prvních 10 řádek vašeho výstupu by mohlo vypadat nějak takto:
Word              Count
=======================
a                 631
a-piece           1
abide             1
able              1
about             94
above             3
absence           1
absurd            2
Kolikrát se v knize objeví slovo alice?
Které je nejdelší slovo v Alice in Wonderland? Kolik má písmen?



# ================================
miko oddel
# ================================
12. Třídy a instance
# ================================

Objektově orientované programování
Vytvoření třídy
Atributy
Inicializační metoda   'init'
Obdélník
Instance jsou měnitelné
Instance jako výstupní hodnoty
Instance uvnitř f-stringu
Kopírování třídy
Dekorátory II
Speciální metody a atributy
Datové třídy
Dědění
Propojení tříd
Glosář
Cvičení

12.1 Objektově orientované programování
Python je programovací jazyk, který podporuje objektově orientované programování (OOP).

Při objektově orientovaném programování je pozornost zaměřena na vytváření objektů, které obsahují jak data, tak funkce či metody.

Téměř vše v Pythonu je objekt. Objekt je kolekce dat (proměnných) a metod (funkcí), které s danými daty pracují. Prototypem objektů jsou třídy, z nichž jsou všechny objekty (čísla, řetězce, funkce, moduly, metody, atp) odvozeny coby instance.


12.2 Vytvoření třídy
Třída je logické seskupení dat a funkcí. Ve své podstatě definuje nový, složený datový typ. Různé vestavěné typy - třídy Pythonu (str, int, float, ...) používáme již od počátečních kapitol.

Nejjednodušší definice třídy vypadá takto:

class Emanuel:
    '''Nepovinný dokumentační řetězec - docstring '''
    pass
Záhlaví složené z klíčového slova class, názvu třídy a dvojtečky je vše, co jednoduchá třída potřebuje.
Později se dovíme, že třída může dědit ze své nadtřídy, v tom případě by před dvojtečkou byl název supertřídy v závorkách - class Emanuel(superClass): .
Následuje odsazené tělo třídy, které bude obsahovat řadu dalších objektů. V naší demonstraci jsme uvedli příklad dokumentačního řetězce a jedno klíčové slovo pass, které nedělá nic. Pro platnost minimální definice postačí jedno z uvedeného.
S naší prostinkou třídou můžeme už provádět řadu regulérních úkonů, například:

vytvořit datový atribut 'strom' třídy Emanuel:
>>> Emanuel.strom = "ořech"
vytvořit samostatný objekt - instanci třídy Emanuel:
>>> eman = Emanuel()
vytvořit datový atribut 'míra' objektu 'eman':
>>> eman.míra = 158
Definice třídy se mohou vyskytnout kdekoli v programu, ale obvykle se umisťují poblíž počátku (po příkazech import).

Pro zvídavé:
Třídy samotné jsou instancemi prvotní třídy type (termín type je synonymem termínu class):

>>> x = [2, 5, 8], y = "Nazdar"
# x, y jsou instancemi tříd list a str:
>>> type(x), type(y)
(<class 'list'>, <class 'str'>)
# list a str jsou instancemi třídy type:
>>> type(type(x)), type(type(y))
(<class 'type'>, <class 'type'>)
# tudíž nepřekvapí že:
>>> type(Point)
<class 'type'>
Nebudeme ale předbihat. Konstrukci třídy si krok po kroku vysvětlíme na konkretním případě třídy Point, kterou si vytvoříme pro manipulaci s bodem ve dvourozměrném prostoru.

Třída Point
Polohu bodu v rovině určíme jeho souřadnicemi. V matematickém zápisu bodu se tyto souřadnice, oddělené čárkou, uvádějí v závorce. Například, (0, 0) představuje počátek souřadnic, (x, y) představuje bod ve vzdálenosti x ve vodorovném a y ve svislém směru od počátku.

class Point:
    pass
Vytvořením třídy vytvoříme prototyp možných konkrétních objektů, neboli instancí  třídy. Vytvoření nové instance připomíná volání funkce:

>>> p = Point()             # vytvoření objektu (instance třídy)
Ke třídě Point se vrátíme v odstavci 12.4.


12.3 Atributy
Slovem atribut označujeme obecně vlastnosti nějakého objektu, v tomto případě jím označujeme vlastnosti třídy a instance. Atributy třídy i instance jsou dvojího druhu - datové a funkční.

Datovými atributy jsou proměnné, funkčními atributy jsou metody, což jsou funkce, definované uvnitř třídy a volané pro instanci (objekt) tečkovou notací. Atributem je také případný dokumentační řetězec.

Datové atributy
Pro instanci i třídu lze určit atributy i dodatečně (jak jsme již viděli v předběžné ukázce):

>>> p.x = 3                # datový atribut 'x' instance 'p'
>>> p.y = 4                # datový atribut 'y' instance 'p'

>>> Point.a = "alef"       # datový atribut 'a' třídy Point
Tato skladba je podobná skladbě pro výběr atributu z modulu, např. math.pi nebo string.ascii_uppercase. Jak moduly, tak i třídy a instance vytvářejí své vlastní jmenné prostory. Přístup k jejich jménům (atributům) je v obou případech stejný - přes tečkovou notaci. V naší ukázce vytváříme atributy tím, že jim přiřazujeme hodnoty.

Ověřme si to:

>>> p.x, p.y
(3,4)
>>> Point.a
'alef'
Tečkovou notaci můžeme použít jako součást jakéhokoliv výrazu, takže následující příkazy jsou legální:

>>> print('%d  %d' % (p.x, p.y))
3 4
>>> print(p.x*p.x + p.y*p.y)
25
Stejně snadné jako vytvoření objektu a deklarace jeho atributů (případně atributů třídy), je jejich smazání příkazem del:

>>> del p.y
>>> del Point.a
>>> del p
Metody
Pro třídu v Pythonu se rozlišují tři metody: instanční, statická a metoda třídy:

Instanční metoda definuje chování objektu (instance), nikoli třídy. Definice obsahuje parametr self. V odstavci 12.4 uvedená speciální metoda __init__ je eminentní metoda instanční.
class Sample:                         deklarace třídy
    val = 10                          datový atribut třídy
    def myFunc(self):                 metoda instance
        print("Value: ", self.val)
>>> obj = Sample()                    vytvoření instance
>>> obj.myFunc()                      volání metody
Value:  10
Metoda třídy definuje chování celé třídy, nikoli objektu. Definice obsahuje parametr cls a je uvedena vestavěným dekorátorem @classmethod.
Tato metoda má přístup k proměnné třídy a ke statické metodě, nemá přístup k datům instance.
class Hample:
    ham = 20                          datový atribut třídy

    @classmethod                      dekorace
    def myFunc(cls):                  metoda třídy
        print("Hodnota proměnné třídy: ", cls.ham)
        cls.otherFunc()               volání staticé metody

    @staticmethod                     dekorace
    def otherFunc():                  statická metoda
        print("Výstup statické metody.")
>>> Hample.myFunc()                   volání metody třídy
Hodnota proměnné třídy:  20           výstup metody třídy
Výstup statické metody.               výstup statické metody
Statická metoda je obyčejná funkce, deklarovaná uvnitř třídy. Deklarace je uvedena vestavěným dekorátorem @staticmethod (viz odst. 12).
Tato metoda má přístup pouze ke svým vlastním atributům. Obě metody lze volat i přes vytvořenou instanci:
>>> hamp = Hample()
>>> hamp.myFunc()
Hodnota proměnné třídy:  20
Výstup statické metody.
>>> hamp.otherFunc()
Výstup statické metody.

12.4 Inicializační metoda __init__
Protože naše třída Point má představovat matematické body v dvojrozměrném prostoru, všechny její instance by automaticky měly mít atributy x a y. Tak tomu však u našich objektů třídy Point zatím není:

>>> p2 = Point()            # vytvořili jsme instanci

>>> p2.x = 8                # vytvořili jsme atribut přiřazením hodnoty
>>> p2.y                    # bez přiřazení atribut 'y' neexistuje!
Traceback (most recent call last):
    File "<stdin>", line 1, in?
AttributeError: Point instance has no attribute 'y'
>>>
Abychom při každé deklaraci objektu nemuseli vytvářet jeho datové atributy ručně, použijeme takzvanou inicializační metodu __init__, kterou přidáme na začátek třídy a pomocí níž potřebné atributy objektu zavedeme předem. Této funci (metodě) se také říká konstruktor.

 class Point:
     def __init__(self, x=0, y=0):
         self.x = x
         self.y = y
Prvním parametrem definice __init__ je povinné slovo self, které zastupuje dosud neexistující (ale předpokládanou) instanci třídy. Další parametry s počáteční hodnotou zajišťují, že každá nově vytvořená instance bude implicitně obsahovat datové atributy x, y, zde s počáteční nulovou hodnotou.

Užitečnost konstruktoru si ukážeme ve spojení s další metodou, která určí vzdálenost bodu od počátku souřadnic:

 class Point:
     def __init__(self, x=0, y=0 ):           # konstruktor
         self.x = x
         self.y = y
     def distance_from_origin(self):          # metoda instance
         return(self.x**2 + self.y**2)**0.5
Při vytváření instance musíme zadat hodnotu atributů, deklarovaných v metodě __init__. Pokud jsou tyto atributy deklarovány s počátečními hodnotami, které nám vyhovují - potom nemusíme:

>>> p = Point()
>>> p.x, p.y
(0, 0)
Můžeme zajisté vytvořit objekt s vlastními hodnotami x,y:
>>> g = Point(3,4)
>>> g.x, g.y
(3, 4)
>>> g.distance_from_origin()
5.0
Instance jako parametr
Instanci můžeme zadat jako parametr obvyklým způsobem:

def print_point(obj):
    print('%s, %s' % (obj.x, obj.y))
>>> print_point(g)
3, 4
>>> print_point(p)
0, 0

12.5 Obdélník
Řekněme, že chceme, aby třída představovala obdélník. Otázkou je, jakou informaci musíme poskytnout, abychom určili obdélník? Pro zjednodušení předpokládejme, že je obdélník orientován buďto vodorovně nebo svisle, nikdy není pootočen.

Máme několik možností: můžeme určit střed obdélníka (dvě souřadnice) a jeho velikost (šířku a výšku), nebo můžeme určit jeden z jeho rohů a velikost, nebo můžeme určit polohu dvou protilehlých bodů. Zvolíme si levý horní roh obdélníka a jeho velikost.

class Rectangle:
    def __init__(self, posice, w, h):
        self.corner = posice
    self.width = w
    self.height = h
Parametr 'posice' předpokládá zadání dvojice čísel - entici. Pro její vložení můžeme použít nepojmenovaný objekt již deklarované třídy Point (první definice v odst. 12.4):
>>> bod = Rectangle(Point(), 100, 200)
>>> bod.width, bod.height
(100, 200)
>>> bod.corner.x, bod.corner.y
(0, 0)
Objektu Point() jsme nezadali žádné argumenty, protože nám zřejmě vyhovují jeho implicitní hodnoty. Kdybychom chtěli mít počátek obdélníka jinde než v bodě (0,0), mohli bychom například zadat:

>>> box = Rectangle(Point(10,50), 100, 200)
>>> box.corner.x, box.corner.y
(10,50)
>>> box.width, box.height
(100,200)
Vzájemné vztahy objektů vidíme na následujícím obrázku: atribut 'corner' objektu 'box' odkazuje na objekt třídy Point s atributy 'x' a 'y'.




12.6 Instance jsou měnitelné
Změnu instance můžeme provést změnou některého z jejich atributů a to přiřazením. Abychom například změnili velikost obdélníka bez změny jeho polohy, změníme hodnoty width a height:

box.width = box.width + 50
box.height = box.height + 100
Změnu atributů můžeme zobecnit do funkce:

def grow_rectangle(obj, dwidth, dheight):
    obj.width += dwidth
    obj.height += dheight
Můžeme také napsat funkci pro změnu polohy obdélníka:

def move_rectangle(obj, dx, dy):
    obj.corner.x += dx
    obj.corner.y += dy

12.7 Instance jako výstupní hodnoty
Instance může být výstupní hodnotou funkce. Například, funkce find_center přijímá instanci třídy Rectangle jako argument a vrací instanci třídy Point, která obsahuje souřadnice středu zadaného obdélníka:

def find_center(obj):
    p = Point()
    p.x = obj.corner.x + obj.width/2.0
    p.y = obj.corner.y + obj.height/2.0
    return p
Když si definice tříd Point (odst. 12.4), Rectangle (odst 12.6) a funkcí find_center, print_point vložíme do jednoho skriptu, můžeme v konzole Pythonu psát:

>>> box = Rectangle(Point(40,60), 100, 200)
>>> center = find_center(box)
>>> print_point(center)
90.0, 160.0
Je také možné deklarovat instanci s použitím entice,

>>> boot = Rectangle((40,60), 100, 200)
instance obsahuje atribut 'corner' ale hodnoty tohoto atributu nemají jména:

>>> boot.corner
(40,60)
>>> boot.corner.x
AttributeError: 'tuple' object has no attribute 'x'
Pro takto deklarovaný objekt nám samozřejmě nebudou chodit funkce distance_from_origin(), print_point(obj) (ods. 12.4) a find_center(obj) (odst. 12.7), protože všechny používají jména x,y. Bude nám chodit funkce grow_rectangle(obj,dwidth,dheight) (odst. 12.6).


12.8 Instance uvnitř f-stringu
Instanci lze reflektovat i uvnitř f-stringu (viz kap. 6.17 Formátování řetězců III). Máme-li například definovanou třídu v souboru katalog.py:

class Komik:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, věk {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, věk {self.age}. Překvapení!"
můžeme ji importovat do interaktivní konzoly, vytvořit instanci a tu posléze aktivovat v f-stringu:

>>> import katalog
>>> komik = katalog.Komik("Jan", "Plíšek", "74")
>>> f"{komik}"               případně  f"{komik!s}"
'Jan Plíšek, věk 74.'
>>> f"{komik!r}"             viz 6.16 Formátování řetězců II
'Jan Plíšek, věk 74.  Překvapení!'      viz soubor katalog.py
Poznámku Překvapení! jsme při uplatnění konverze !r ve výměnném poli získali proto, že jsme si ji nadefinovali v metodě __repr__(self).


12.9 Kopírování třídy
Při kopírování třídy či objektu třídy (instance) použijeme vždy metodu copy nebo deepcopy z modulu copy.
Pro objekty tříd, které neobsahují vnořené objekty, postačí tak zvaná mělká kopie (shallow copy), která vytvoří nezávislou kopii nevnořených objektů. Příkladem takového objektu je třída Point z odst. 12.4:

>>> import copy

>>> p1 = Point(3,4)
>>> p2 = copy.copy(p1)
>>> p1 is p2
False                          # mají různá ID
>>> p1.x == p2.x and p1.y == p2.y
True                           # mají stejné souřadnice
Příkladem vnořeného objektu je atribut corner třídy Rectangle , jejíž dva nevnořené objekty jsou atributy x, y - viz odst. 12.6.

Vytvoříme-li obdélník b1 a jeho kopii b2 funkcí copy,

>>> b1 = Rectangle(Point(), 100, 200)
>>> b2 = copy.copy(b1)
vytvoří se nezávislé kopie pouze atributů with a height, zatímco atribut corner je společný pro obě prezentace b1 a b2:


Nezávislou hlubokou kopii (deep copy) i vnořených objektů vytvoříme metodou deepcopy:

>>> b2 = copy.deepcopy(b1)

12.10 Dekorátory II
Dekorace funkce funkcí je popsána v kapitole 3.11.

Dekorace funkce třídou
Při dekorování funkce třídou zastupuje klauzuru 'wrapper' speciální metoda __call__:

class Pohoda:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        # Sem může přijít vhodný kód
        self.fun(*args, **kwargs)            # volání 'ovečky'
        # Sem rovněž může přijít vhodný kód

@Pohoda                                      # dekorace třídou
def pozdrav(name, message ='Nazdar'):        # ovečka
    print("{} {}".format(message, name))
>>> pozdrav("Pavle!")
Nazdar Pavle!
Uvedená ukázka je poněkud schematická, protože výstup "Nazdar Pavle!" bychom zajistili i bez dekorátoru. Napravíme to další ukázkou, ve které nám dekorátor doplní výstup z dekorované třídy:

class Decorator:
   def __init__(self, x):
        self.x = x

   def __call__(self, a):
        print('Druhá mocnina', a, 'je', self.x(a))
                             # výraz self.x(a) je invokace ovečky
@Decorator
def square(a):
   return a*a
>>> square(5)
Druhá mocnina 5 je 25
Dekorace třídy funkcí
import functools
import time

def timer(func):
    "Vytiskne délku výpočtu dekorované funkce či třídy"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        run_time = time.perf_counter() - start
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return val
    return wrapper

@timer
class Calculator:
    def __init__(self, num):
        self.num = num
        import time
        time.sleep(2)

    def double_and_add(self):
        "Vrátí sumaci stejně modifikovaných členů řady"
        res = sum([i * 2 for i in range(self.num)])
        print("Result : {}".format(res))
>>> c = Calculator(100)
Finished 'Calculator' in 2.0111 secs
>>> c.double_and_add()
Result : 9900
Dekorátor @timer můžeme použít i k dekoraci funkce.


12.11 Speciální metody a atributy
Pro zvídavé
Speciální (také magické) jsou všechny předdefinované metody a atributy tříd, jejichž název je ohraničen dvěma podtržítky, jako například výše popsaná metoda __init__. Jejich alternativní označení v angličtině je dunders (double underscores).

Výpis předdefinovaných metod a atributů pro určitý objekt získáme příkazem dir(), například pro slovník (list):

>>> dir([1,2,3])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
 '__lt__',  '__mul__', '__ne__', '__new__', '__reduce__',  '__reduce_ex__',
 '__repr__', '__reversed__',  '__rmul__', '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__',
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
 'pop', 'remove', 'reverse', 'sort']
Speciální metody jsou interně evokované při explicitním volání příslušných operátorů a vestavěných funkcí. Například porovnání "ariel" == "alias" je realizováno speciální metodou __eq__:

>>> "ariel".__eq__("alias")
False
Speciální metodě můžeme zadat specifické chování. Například sečíst souřadnice dvou bodů (provést vektorový součet):

class Point:
    def __init__(self, x=0, y=0):        # speciální metoda (instanční)
        self.x = x
        self.y = y

    def __add__(self, other):            # speciální metoda (instanční)
        return self.x + other.x, self.y + other.y
>>> p1 = Point(1, 2)
>>> p2 = Point(3, 4)
>>> p1 + p2                       # interně  p1.__add__(p2)
(4, 6)
Specielními atributy jsou datové objekty __doc__, __name__, __dict__, ... . Atribut __doc__obsahuje informaci o příslušném objektu; například o prázdném seznamu se dozvíme:

>>> [].__doc__
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
Dobrý přehled specielních metod lze nalézt na stránce tutoriálu Ponořme se do Pythonu 3


12.12 Datové třídy
Datová třída (dataclass) je speciální třída, vhodná pro ukládání datových objektů, která je vytvořená s pomocí dekorátoru @dataclass, importovaného z modulu dataclasses.

Tento dekorátor automaticky generuje všechny potřebné dunder metody (__init__(), __repr__(), ...), podporující zjednodušené zadávání datových atributů, zde zvaných pole (fields). Deklarace pole má skladbu:   name:   type   [ = value ].

dunder: společné označení metod, jejichž názvy jsou vymezeny dvojitými podtržítky (double-underscore).

from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    email: str
    phone: str = "00 00 00 00"
>>> contact = Contact("test","test@test.com", '72 63 08 56')
>>> contact
Contact(name='test', email='test@test.com', phone='72 63 08 56')
Lze použít také klíčové argumenty:

>>> contact1 = Contact(name="test1",email="test1@test.com")
>>> contact1
Contact(name='test1', email='test1@test.com', phone='00 00 00 00')

12.13 Dědění
Mechanizmus, zvaný dědění (inheritance) se používá při odvození nové třídy z třídy stávající. Odvozená třída (sub class, sub typ, potomek) přebírá atributy a metody (bázové) třídy výchozí (super class, rodič či předek).

Skladba pro deklaraci subtřídy je jednoduchá:

class NázevOdvozenéTřídy(NázevVýchozíTřídy):
    '''Nepovinný dokumentační řetězec - docstring '''
    pass
Kromě naznačeného dědění po jediném předkovi (simple heritance) existují další možnosti:

multiple inheritance - prosté dědění po různých předcích: class Potomek(Parent1, Parent2)
multilevel inheritance - zanořené dědění po více předcích: class Potomek(Parent), class Vnuk(Potomek)
Instruktivní ukázka s použitím speciální metody __init__:

class Savci:
    vid = "Pozdrav Pánbůh"
    def __init__(self, druh):
        hid = "pane Randák"
        print(druh, 'je teplokrevný savec.')

class Pes(Savci):
    def __init__(self):
        super().__init__('Pes')            Varianta: Savci.__init__(self, 'Pes')
        print('Pes je přítel člověka.')
Speciální metoda __init__ třídy Pes potlačí tutéž metodu třídy Savci. Toto chování však zruší následně definovaná metoda __init__ s objektem super() (nebo Savci), čímž umožňuje použití atributů děděné třídy.

>>> pajda = Pes()
Pes je teplokrevný savec.
Pes je přítel člověka.
Zadání: Vypusťte v definici třídy Pes řádek "super().__init__('Pes')" a a zkuste pro objekt pajda volat proměnné vid a hid.

Obsahuje-li zdrojová i děděná třída stejný atribut, platí pro děděnou třídu vlastní definice tohoto atributu:

class A:
    pes = "Dingo"
    def zobraz(self):
        print ('Jsem třída A.')

class B(A):
    pes = "Voříšek"
    def zobraz(self):
        print ('Jsem třída B.')
>>> obj = B()
>>> obj.pes
'Voříšek'
>>> obj.zobraz()
Jsem třída B.

12.14 Propojení tříd
Propojení tříd lze kromě dědění provést také takzvanou kompozicí. Propojení se uskuteční prostřednictvím instance třídy uvnitř jiné třídy:

class Raketa:
    def __init__(self, name, destinace):
        self.name = name
        self.distance = destinace

    def launch(self):
        return "%s dosedl na %s" % (self.name, self.destinace)

class Lunochod():
    def __init__(self, name, destinace, maker):
        self.raketa = Raketa(name, destinace)   # deklarace instance
        self.maker = maker

    def report(self):
        return "%s byl spuštěn korporací %s" % (self.raketa.name, self.maker)
>>> z = Lunochod("Lunochod", "Měsíc", "EKA")
>>> z.raketa.launch()
'Lunochod dosedl na Měsíc'
>>> z.report()
'Lunochod byl spuštěn korporací EKA'

12.15 Glosář
třída (class)
Uživatelsky definovaný typ. Třídu lze považovat za prototyp objektů, určující jejich vlastnosti a chování.
instance
Konkrétní objekt určité třídy.
objekt (object)
Všechno v Pythonu je objekt. Zejména 'instance' se často označuje jako objekt.
konstruktor (constructor)
Metoda __init__, kterou Python automaticky použije při tvorbě nové instance.
atribut (attribute)
Společné označení pro proměnné třídy i objektů a metody.
mělká rovnost (shallow equality)
Rovnost odkazů, nebo dvou odkazů, které ukazují na stejný objekt.
hluboká rovnost (deep equality)
Rovnost hodnot, nebo dvou odkazů, které ukazují na objekty se stejnými hodnotami.
mělká kopie (shallow copy)
Kopie objektu včetně odkazů na vnořené objekty provedená příkazem copy.copy(item); vnořené objekty se nezkopírují, pouze odkazy.
hluboká kopie (deep copy)
Kopie objektu včetně jeho vnořených objektů provedená příkazem copy.deepcopy(item)

12.16 Cvičení
Do třídy Rectangle vložte metodu area, která vrací plochu obdélníka
r = Rectangle(Point(0,0), 50,100)
# test: r.area() --> 5000
Do třídy Rectangle vložte metodu perimeter, která vrací obvod obdélníka
r = Rectangle(Point(0,0), 50,100)
# test: r.perimeter() --> 300
Do třídy Rectangle vložte metodu flip, která zamění jeho šířku za výšku a obráceně
Ke třídě Point (viz 12.4) přidejte metodu sklon, která vrátí úhel sklonu spojnice bodu x,y s počátkem 0,0 v radiánech. Její evokace může vypadat takto:

>>> Point(4,10).sklon()
Sklon v radiánech:  1.1902899496825317
Ošetřte případ, kdy je spojnice kolmá k ose x (ψ = π/2).

Upravte skript třídy Punktum:

class Punktum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Souřadnice bodu: x = {self.x}," \
                                f"y = {self.y}"
tak aby její volání mělo následující výstup

>>> Punktum(5,9)
Souřadnice bodu: x = 5, y = 9


# ================================
miko oddel
# ================================
13. Rekurze a iterace
# ================================

Rekurzivní datové struktury
Rekurze II
Memoizace
Iterátory
Generátory
Chyby a výjimky
Glosář
Cvičení

13.1 Rekurzivní datové struktury
Všechny dosud poznané datové typy mohou být v seznamech a enticích uspořádány přerůzným způsobem. Seznamy a entice mohou být také vnořené.

Povšimněme si, že termín seznam s vnořenými seznamy  je použit ve své vlastní definici. Rekurzivní definice jako tato jsou zcela obvyklé v matematice a v programování. Poskytují stručný a účinný způsob popisu rekurzivních datových struktur, které jsou částečně složeny z menších a jednodušších výskytů sebe sama. Nejedná se o definici v kruhu, neboť v jisté úrovni dospějeme k seznamu, který nemá žádné položky, jež by byly seznamem.

Předpokládejme, že našim úkolem je napsat funkci, která sečte všechny hodnoty v seznamu s vnořenými seznamy. Python má vestavěnou funkci, která vytvoří součet řady čísel:

>>> sum([1, 2, 8])
11
>>> sum((3, 5, 8.5))
16.5
>>>
Pro náš seznam s vnořenými seznamy však funkce sum nepracuje:

>>> sum([1, 2, [11, 13], 8])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>>
Problém spočívá v tom, že třetí položka seznamu je také seznam [11, 13], který nemůže být přičten k 1, 2, a 8.


13.2 Rekurze II
Tento text je pokračováním části 4.5 - Rekurze I.

K vytvoření součtu všech čísel v našem rekurzivním seznamu s vnořeným seznamem potřebujeme traverzovat seznamem, navštívit každou číselnou položku uvnitř vnořené struktury a připočítávat číselné hodnoty k našemu součtu.

Potřebný program pro vytvoření součtu čísel v seznamu s vnořeným seznamem je díky rekurzi překvapivě krátký:

def recursive_sum(nested_num_list):
    sum = 0
    for element in nested_num_list:
        if type(element) == type([]):        # je-li položkou seznam
            sum = sum + recursive_sum(element)
        else:
            sum = sum + element
    return sum
Tělo fce se skládá hlavně ze smyčky for, která traverzuje seznamem nested_num_list. Je-li položkou seznamu numerická hodota nikoliv seznam (větev else), přičte se číslo jednoduše k proměnné sum. Je-li položkou seznam, potom je opět volána fce recursive_sum pro argument, jímž je vnořený seznam. Příkaz uvnitř těla funkce, jímž je volána táž funkce, se nazývá rekurzivní volání.

Poněkud komplikovanější úlohou je nalezení největší hodnoty v seznamu s vnořeným seznamem. Následující definice funkce obsahuje doctest (viz kap. 5.10), kterým si jednak ilustrujeme řešený problém a zároveň ověříme správnost naší funkce:

def recursive_max(nested_num_list):
    """
    >>> recursive_max([2, 9, [1, 13], 8, 6])
    13
    >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
    100
    >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
    100
    >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
    100
    """
    largest = nested_num_list[0]
    while type(largest) == type([]):
        largest = largest[0]

    for element in nested_num_list:
        if type(element) == type([]):
            max_of_elem = recursive_max(element)
            if largest < max_of_elem:
                largest = max_of_elem
        else:            # element is not a list
            if largest < element:
                largest = element

    return largest
Čertovým kopýtkem tohoto problému je určení numerické hodnoty pro inicializaci proměnné largest. Nemůžeme jednoduše zadat, že je to nested_num_list[0], protože by touto položkou mohlo být jak číslo, tak seznam. Problém je řešen použitím smyčky while, která přiřadí proměnné largest první číselnou hodnotu bez ohledu na hloubku jejího vnoření.

Nekonečná rekurze
Při rekurzivním volání téže funkce se generuje řada výsledků, z nichž jeden má být určen jako výstup volání posledního. Takový výsledek se nazývá základní případ (base case). Bez základního případu dostaneme nekonečnou rekurzi. Tato situace je technicky ošetřena tak, že se Python zastaví po dosažení implicitně nastavené hloubky rekurze (1000 cyklů) a vrací chybu při běhu programu.

Ve funkci recursive_sum je počet rekurzivních volání určen počtem prvků v seznamu. Základní případ zde poskytuje skrytá funkce next() idiomu FOR i IN iterable (viz odst. 13.4 Iterátory). Ve funkci countdown(n) (s koncovou rekurzí) je základním případem hodnota n = 0.

Příkladem nekonečné rekurze budiž tato funkce:

#
# infinite_recursion.py
#
def recursion_depth(number):
    print("Recursion depth number {}." .format(number))
    recursion_depth(number + 1)

recursion_depth(0)
Ve stejném adresáři, ve kterém máte uložený svůj program, zapište na příkazový řádek:

python infinite_recursion.py
Po bezmocném sledování ubíhajících řádků na monitoru se po chvíli dočkáte následujícího konce záznamu:

  ...
  File "infinite_recursion.py", line 3, in recursion_depth
    recursion_depth(number + 1)
RuntimeError: maximum recursion depth exceeded
Nekonečná rekurze může být těžko něčemu prospěšná, takže si při každé deklaraci rekurzivního volání bedlivě ohlídáme okrajové podmínky, vytvářející základní případ.

Koncová rekurze
Když se rekurzivní volání objeví na posledním řádku těla funkce, označujeme jej jako koncovou rekurzi.

Zde je koncová rekurze použita u funkce countdown:

def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
Mnohé dobře známé matematické funkce jsou definovány rekurzivně. Například Fibonacciho číslo, nebo fibonacciho sekvence, definovaná:

fibonacci(0) = 1
fibonacci(1) = 1
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
To lze také snadno přepsat do Pythonu:

def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
Kód pro fibonacci je příkladem koncové rekurze.

Koncová rekurze je však v Pythonu považována za špatnou techniku, protože používá více systémových zdrojů než ekvivalentní iterativní řešení.

Volání fibonacci(500) uvede interpreta Pythonu do rozpaků.

Mnohem rychlejší než rekurzivní verze je verze iterační, která by mohla vypadat takto:

def fiboiter (n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
    old, new = new, old + new
    return  new
Vyzkoušejte volání fibointer(500) a budete příjemně překvapeni.
Při cvičení si zkusíte napsat iterační verzi funkce factorial a v dalším odstavci si ukážeme memoizovanou alternativu funkce fibonacci, která je ze všech tří verzí nejrychlejší.


13.3 Memoizace
Když jsme si v předchozím odstavci pohrávali s funkcí fibonacci, mohli jsme si všimnout, že čím větší argument jsme použili, tím déle trvalo provádění funkce. Se zvětšujícím se argumentem časové nároky velmi rychle rostly. Na jednom z našich počítačů končí fibonacci(20) okamžitě, fibonacci(30) zabere asi vteřinu a fibonacci(40) trvá zhruba věčnost.

Abychom pochopili proč, pohleďme na toto schéma volání funkce fibonacci(4):



Schéma zobrazuje sadu funkcí v rámečcích se šipkami, ukazujícími na volané funkce. Nejvýše umístěná fce, fibonacci(4) volá fibonacci(3) a fibonacci(2). Fce fibonacci(3) zas volá fibonacci(2) a fibonacci(1). A tak dále.

Spočítejme, kolikrát je voláno fibonacci(0) a fibonacci(1). Je to řešení neefektivní a rychle se zhoršuje při zvětšujícím se argumentu.

Dobrým řešením, zvaným memoizace (memoization), je ukládat si záznamy (hints) o spočítaných hodnotách do slovníku pro potřebu dalšího použití. Takovýmto záznamům říkejme třeba náznaky. Zde vidíme realizaci funkce fibonacci s podporou náznaků:

memo = {0:0, 1:1}
def fibomem(n):
    if n not in memo:
        memo[n] = fibomem(n-1) + fibomem(n-2)
    return memo[n]
Slovník memo zaznamenává fibonacciho čísla, která již známe. Začínáme pouhými dvěma páry: 0 ukazuje na 0, 1 na 1.
Kdykoli je funkce fibomem volána, prozkoumá svůj slovník, zda neobsahuje výsledek. Jestliže ano, vrací výsledek bez dalších okolků. Jestliže ne, počítá novou hodnotu. Tato hodnota je přidána do slovníku před tím, než se funkce vrátí k rekurzivnímu volání.

S použitím této verze náš počítač spočítá fibonacci(50) v jednom oka mžiku.

>>> fibomem(100)
354224848179261915075
Alternativní způsob výpočtu Fibbonacciho čísla pomocí memoizace představuje výpočet s podporou dekorátorů (viz kap.3.11 a kap. 12.12):

def memoize(fun):                # dekorátorová funkce
    memo = {}
    def wrapper(x):
        if x not in memo:
            memo[x] = fun(x)
        return memo[x]
    return wrapper

@memoize                         # dekorace funkcí
def fibomem(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibomem(n-1) + fibomem(n-2)

# >>> fibomem(100) ==> 354224848179261915075
class Memoize:                    # dekorátorová třída
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize                         # dekorace třídou
def fibomem(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibomem(n-1) + fibomem(n-2)

# >>> fibomem(100) ==> 354224848179261915075
Všechny tři způsoby používají slovník memo a podmínku if x not in memo:.


13.4 Iterátory
Iterátor je interní objekt, jenž vlastní metody __iter__() a __next__(), které vracejí hodnotu následného elementu při každé své invokaci.

Iterátor se vytváří čtverým způsobem:

Použitím funkce iter - viz kap. 4.6.
Skrytě, pro interní potřebu idiomu for... či funkce open(...), min(), max(), map(), filter(), zip(), enumerate() a reversed().
Pomocí generátorové funkce a generátorového výrazu, jejichž výstupem jsou iterátory, které provádějí takzvaný líný výpočet (lazy evaluation).
Vytvořením třídy s definovanými metodami __iter__() a next(). Takto definovaný iterátor líný výpočet neprovádí.
Iterátory definované třídou
Iterátorem v tomto případě je instance třídy s definovanými metodami __iter__()  a next().

Jako příklad si uvedeme skript, který si poté pustíme v konzole:

class CountTo:
    def __init__(self, m):
        self.m = m-1
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= self.m:
            cur, self.n = self.n, self.n + 1
        return cur
        else:
            raise StopIteration()
>>> cnt = CountTo(5)     # instance třídy a zároveň iterátor
>>> next(cnt)            # první iterace
0
>>> for i in cnt: print(i, end=" ")
1 2 3 4                  # opakovaná iterace pro zbytek členů
>>> for in cnt: print(i, end=" ")
...                      # zdvořilé mlčení, iterátor je prázdný
Alternativa funkce squares(start, stop) ve tvaru uživatelského iterátoru může mít tento tvar:

class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current
>>> sqr = Squares(4,8)          # instance třídy a zároveň iterátor
>>>
>>> for i in sqr: print(i, end=" ")
16 25 36 49                     # dychtivá (eager) iterace
>>> for in sqr: print(i, end=" ")
...                             # zdvořilé mlčení, iterátor je prázdný

13.5 Generátory
Generátor je objekt, vytvořený aplikací generátorového výrazu, případně voláním generátorové funkce. Generátor je iterátor, který místo hotových objektů ukládá instrukce pro jejich individuální vytvoření při iteraci.

Generátorový výraz
Generátorový výraz je vytvořen komprehenci entice (viz 8.10).

>>> st = "abakus"                     # iterovatelný řetězec - iteráble
>>> stv = (i for i in st)             # generátorový objekt - iterátor
>>> for i in st: print (i, end=" ")   # dychtivá (eager) iterace iteráblu
a b a k u s
>>> for i in stv: print (i, end=" ")  # líná (lazy) iterace iterátoru
a b a k u s
Generátorový výraz lze vytvořit i s použitím idiomu for pro funkci range(~). Zde funkce range() vytvoří iterovatelný objekt, který se komprehencí přemění na iterátor:

>>> gv = (i*i for i in range(5))        # generátorový objekt - iterátor
>>> for i in gv: print (i, end=", ")    # líná (lazy) iterace
0, 1, 4, 9, 16
Generátorová funkce
Generátorová funkce musí obsahovat alespoň jeden příkaz yield. Volání generátorové funkce vrací generátorový objekt, jenž je iterátorem s přímo použitelnou funkcí next(~) či metodou __next__() - stejně jako v předchozím případě:

def count_to(m):
   n = 0
   while n <= m:
      yield n              # poskytuje elementy iterátoru
      n += 1
========== RESTART: F:\Codetest\HowTo\trump.py ==========

>>> ct = count_to(5)                  # generátorový objekt, iterátor
>>> next(ct)                          # 1. krok dychtivé iterace
0
>>> ct.__next__()                     # 2. krok dychtivé iterace
1
>>> for i in ct: print (i, end=" ")   # líná (lazy) iterace
2 3 4 5
>>> next(ct)
StopIteration                         # iterátor je prázdný
Generátorový objekt vytvoří i tato generátorová funkce:

def squares(start, stop):
    for i in range(start, stop):
        yield i * i
Výpočet řady Fibonacciho čísel můžeme provést pomocí následujícího generátoru:

def fibonacci():
    a, b = 0, 1
    while True:  # nekonečná smyčka!
        yield a
        a, b = b, a+b
Generátor s nekonečnou smyčkou voláme pro konkretní mez:

>>> f = fibonacci()
>>> type(f)        # -->  <class 'generator'>
>>> f.__next__()   # -->  0
>>> next(f)        # -->  1    alternativní verze
...
>>> for i in range(7): print(next(f), end=" ")
1 2 3 5 8 13 21
>>> f.__next__()   # -->  34
Generátorový výraz a generátorová funkce vrací generátorový objekt, který je pomalu (líně) vyhodnocovaným iterátorem.

Líný výpočet
Generátorové objekty podporují líný výpočet (lazy evaluation), při kterém se odkládá výpočet výrazu až do chvíle jeho potřeby. Důsledkem je zmenšená potřeba zdrojů (paměti) při zvýšeném výkonu procedury.

Lze sestavit potenciálně nekonečné struktury, např. smyčky - viz fibonacci().

Líný výpočet se obtížně kombinuje s imperativními strukturami jako je ošetření výjímek nebo vstup/výstup; může vytvářet "space leaks" (viz).

Příkladem procedury, uplatňující líný výpočet, je použití slovníku v kapitole 11.7 Switch case, kde u funkce kalkul(oprerátor, x,y) je řešeno částečné ošetření výjimek.


13.6 Chyby a výjimky
Jak už bylo uvedeno v první kapitole, mohou se při kompilaci kódu vyskytnout chyby skladebné (syntaktické) a chyby za běhu programu takzvané "run-time errors". Oba typy chyb jsou události, které Python umí ošetřit.

Syntaktické chyby
Při výskytu skladebné chyby se zastaví běh kompilace a zobrazí se informace s uvedením inkriminovaného řádku a označením místa na řádku, kde k chybě došlo (celé slovo před znakem ^ - zde za slovem True má být dvojtečka):

>>> while True print ("Nazdar!")
   File "<stdin>", line 1
     while True print ("Nazdar!")
                ^
 SyntaxError: invalid syntax
Výjimky
Výjimka (exception) je systemizovaná chyba, k níž dojde při běhu programu. Výjimky jsou definovány jako třídy, odvozené od třídy BaseException. Úplný výpis těchto tříd lze nalézt v Built-in Exceptions.

Kromě vestavěných (built-in) výjimek (např. TypeError, IndexError, ZeroDivisionError, ... ) je možné používat vlastní typ výjimky vytvořením třídy, odvozené od třídy Exception - viz User defined exceptions.

Při výskytu systemizované chyby (např. dělení nulou) zastaví Python běh programu a zobrazí informaci o vzniklé chybě:

>>> print(55/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
Chybové hlášení na poslední řádce se skládá ze dvou částí: název chyby (neboli třídy-výjimky) před dvojtečkou a podrobnosti o chybě za dvojtečkou.

Ošetření výjimek
Chceme-li zařídit aby po výskytu určité chyby pokračovalo provádění programu, provedeme takzvané "ošetření výjimky" (exception handling).

To zpravidla spočívá v použití příkazu try ... except (případně také else či finally ) dle následujícího schematu:

try:
    do_something()
except:
    handle_exception()
...
Klauzulí except může být v případě potřeby více, případně se jedna klauzule může vztahovat na více výjimek:

... except(RuntimeError, TypeError, NameError):
... pass        # some activity
Pro klauzuli except s určitou standardní výjimkou platí, že tato klauzule se vztahuje také na všechny výjimky, které jsou z uvedené výjimky (třídy) odvozené.

Neuvedeme-li v klauzuli žádnou výjimku, pak tato klauzule platí pro všechny vestavěné výjimky, což nemusí být zrovna to pravé ořechové:

def bad_example(number):
    try:
    return number / 0
    except: # slabá klauzule
    print("Máme chybu, nevíme jakou")
>>> bad_example("aleš")
Máme chybu, nevíme jakou
Příklad s try, except, else:

# Určení přítomnosti či nepřítomnosti souboru

def exists(filename):   # název souboru v uvozovkách
    try:
        f = open(filename)
    except OSError:
        print ("Soubor nenalezen")
    else:
        f.close()
    print ("Soubor existuje a byl zavřen")
Sémantická výhrada: Zjišťovat přítomnost souboru tím, že jej dokážeme otevřít, je poněkud nemotorné. Jednak může dojít k aktualizaci časového razítka, druhak můžeme dostat nesprávnou odpověď jenom proto, že je soubor někde otevřen nebo že k němu nemáme oprávnění.

Vybranější způsob je pomocí metody isfile z modulu os.path:

if os.path.isfile("c:/temp/testdata.txt"):
...
Záměrné vyvolání výjimek
Když program narazí na omezující podmínku, můžeme pro případ jejího nesplnění přinutit program, aby vyvolal (raise) standardní výjimku. Následuje příklad, ve kterém se zkoumá zda uživatelem zadané číslo je nezáporné. Pokud je záporné, oznámí se výjimka.

# learn_exceptions.py

def get_age():
    age = int(input('Uveďte svůj věk: '))
    if age < 0:
        raise ValueError("{0} není platná hodnota".format(age))
    return age

>>> get_age()
Uveďte svůj věk: -15
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "learn_exceptions.py", line 10, in get_age
    raise ValueError("{0} není platná hodnota".format(age)
ValueError: -15 není platná hodnota
>>>
Nebo lze raise použít i pro ošetření vlastní výjimky:

class MyExcept(Exception):
    def: __init__(self, length, atleast)
    Exception.__init__(self)
    self.length = length
    self.atleast = atleast

try:
    s = input("Zadej heslo: ")
    if len(s) < 7:
        raise MyExcept(len(s), 7)
except MyExcept as x:
    print ("MyExceptError: Heslo je krátké ({0}<{1})"
               .format(x.length, x.atleast))
else:
    print ("Heslo je v pořádku")

13.7 Glosář
datová struktura (data structure)
Uspořádání dat pro jejich snadnější použití.
rekurzivní definice (recursive definition)
Definice, která se odkazuje sama na sebe. Aby byla smysluplná, musí obsahovat nerekurzivní základní případ. Tímto se liší od definice v kruhu. Rekurzivní definice často skýtají elegantní způsob vyjádření složitých datových struktrur.
rekurze (recursive call)
Příkaz v rekurzivní funkci, který je volá právě prováděnou funkci (to jest samu sebe).
základní případ (base case)
Větev podmíněného příkazu v rekurzivní funkci, který nevede k rekurzivnímu volání.
nekonečná rekurze (infinite recursion)
Funkce, která rekurzivně volá sama sebe, aniž by dospěla k základnímu případu. Způsobí chybu při běhu programu.
koncová rekurze (tail recursion)
Rekurzivní volání umístěné na konci definice funkce. Tato metoda se příliš nedoporučuje, protože bývá méně účinná než iterativní funkce (see the Wikipedia article on tail recursion for more information).
výjimka (exception)
Chyba při běhu programu, pro níž je k dispozici definice třídy.
ošetřit výjimku (handle an exception)
Zabránit registrované chybě (výjimce) aby ukončila běh programu s použitím příkazů try a except.
vyvolat výjimku (raise)
Aktivovat výjimku s použitím příkazu raise.

13.8 Cvičení
Napište funkci recursive_min, která vrátí nejmenší číselnou hodnotu seznamu s vnořenými seznamy:
def recursive_min(nested_num_list):
    """
    >>> recursive_min([2, 9, [1, 13], 8, 6])
    1
    >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
    1
    >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
    -7
    >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
    -13
    """

Funkce by měla vyhovět všem doctestům.
Napište funkci recursive_count, která vrátí počet výskytů číselné hodnoty target v seznamu nested_number_list:
def recursive_count(target, nested_num_list):
    """
    >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
    4
    >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
    2
    >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
    0
    >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
    6
    """
Funkce vyhoví všem doctestům?
Napište funkci flatten, která vrátí jednoduchý seznam, obsahující všechny honoty z nested_number_list:
def flatten(nested_num_list):
    """
    >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
    [2, 9, 2, 1, 13, 2, 8, 2, 6]
    >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
    [9, 7, 1, 13, 2, 8, 7, 6]
    >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
    [9, 7, 1, 13, 2, 8, 2, 6]
    >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
    [5, 5, 1, 5, 5, 5, 5, 6]
    """
Napište funkci readposint, která vyzve uživatele k zadání kladného celého čísla a vstup ověří. Ukázka průběhu může vypadat takto:
>>> num = readposint()
Please enter a positive integer: yes
yes is not a positive integer.  Try again.
Please enter a positive integer: 3.14
3.14 is not a positive integer.  Try again.
Please enter a positive integer: -6
-6 is not a positive integer.  Try again.
Please enter a positive integer: 42
>>> num
42
>>> num2 = readposint("Now enter another one: ")
Now enter another one: 31
>>> num2
31
>>>
Pro ověření správnosti uživatelského vstupu použijte mechanizmus ošetření výjimky.
Přepište funkci factorial s použitím iterace místo rekurze. Volejte svou funkci pro argument 1000 a změřte jak rychle vrátí výsledek.


# ================================
miko oddel
# ================================
A. Tkinter
# ================================

Úvodní informace
Základní pojmy I
Praktická ukázka I
Základní pojmy II
Praktická ukázka II
A.1   Úvodní informace
Účelem této přílohy je poskytnout úvodní a nutně neúplné informace o navrhování grafických aplikací pomocí Tkinteru. Je to vlastně úvodní kapitola k obsáhlejšímu souboru přeložených textů s příklady: Tkinter Pythonu.

Jednoduché příklady budou čtenáře lákat, aby si je během studia Pythonu příležitostně vyzkoušel, proti čemuž nelze nic namítat. Nutno ale poznamenat, že od grafických objektů se očekává něco víc, než jejich pouhé vykreslení na monitoru.

Jsou to GUI - grafická rozhraní mezí počítačem a uživatelem. Mají sloužit k výměně informací pro navazující programy. Pro tuto úroveň použití je nezbytná poměrně ucelená znalost Pythonu - zejména jeho tříd a objektů.

Předložený text není didakticky komponován. Zaujatý student by se měl zaměřit zejména na řízení událostí a používání kontrolních proměnných. Tento čtenář by také měl částečně umět anglicky aby byl schopen si vyhledat chybějící informace.

Programy Tkinteru lze ve Windows psát a editovat v prostředí PyScripter, jejich spouštění je ale nezbytné z dosovské či unixové konzoly, nacédované do složky, do které jsou jednotlivé skripty ukládány.

PyScripter i IDLE jsou aplikacemi Tkinteru a při zavírání skriptů se smyčkou mainloop mívají různé problémy, na které reagují většinou tím, že "zamrznou".

Základní texty o Tkinteru jsou tyto:

Frederic Lundh (1999) - An Introduction to Tkinter
John W. Shipman NMT (2013) - Tkinter 8.5: a GUI for Python
Nás bude zejména zajímat již výše uvedený   Tkinter Pythonu



A.2   Základní pojmy I
Tkinter (či tkinter pro Python 3) je paket modulů, které obsahují kolekce tříd a metod pro přístup k prvkům Tk.

Tk je knihovna rutin v jazyce C neboli sada nástrojů pro správu oken a událostí, která je součástí Tcl
Tcl (Tool Command Language) je jazyk pro manipulaci s prvky Tk.
Widget je prvek grafického rozhraní jako je text box, combo box nebo okno nejvyšší úrovně. Od této chvíle mu budeme familiárně říkat piškot. Piškoty jsou hierarchicky uspořádatelné objekty, vytvořené jako instance tříd.
Termín widget alias piškot má dvojí "skupenství". Jednak to je instance třídy ve skriptu, jednak to je zobrazený prvek na monitoru.ttk je novější modul Tkinteru (Tk 8.5 - prosinec 2007), obsahující odlišné verze většiny standardních piškotů.
GUI (Graphical User Interface) je grafická aplikace, umožňující výměnu informací mezi uživatelem a počítačem. Technicky se skládá z jednotlivých widgetů.
Grafická aplikace se skládá ze tří skupin nástrojů:

piškotů (widgets)
správy geometrie (geometry management)
řízení událostí (event handling)
A.3   Praktická ukázka I
Mnohé náležitosti Tkinteru si nejlépe ukážeme na příkladě (hello1.py)

1   from tkinter import*
2
3   root = Tk()
4   w = Label(root, text="Nazdar světe!")
5   w.pack()
6
7   root.mainloop()
C:\CodeTest\tk-py> python33 hello.py
Tímto prostinkým skriptem vytvoříme okno, které má tři ovládácí prvky a náš popisek "Nazdar světe" :


Jednotlivé řádky skriptu mají tento význam:

Na prvním řádku importujeme modul tkinter; kdybychom chtěli použít také modul ttk, napíšeme na druhý řádek import ttk.
---
Jméno root je náš název pro instaci třídy Tk, která představuje nejvýše postavené okno se základními ovládacími prvky. Do tohoto okna se ukládají všechny další piškoty.
Jméno w je náš název pro instanci třídy Label, která je podřízená objektu root a nese námi vložený text.
Nezbytný úkon, který zviditelní předtím deklarovaný objekt. Jde o akt správy geometrie, který si označíme jako expozici neboli výstav.
---
Poslední instrukce evokuje metodu mainloop() pro objekt root, která generuje nekonečnou smyčku událostí.
A.4   Základní pojmy II
Nekonečná smyčka událostí mainloop je velmi důležitou a sofistikovanou částí programové struktury. Zobrazení okna si můžeme představit jako promítání filmu, při kterém si vůbec neuvědomujeme střídání jednotlivých políček.

Zobrazení není statické ale cyklicky se obnovuje tak dlouho, dokud není dalším příkazem ukončeno.
V našem případě ukončí opakované zobrazování okna klik myší na ovládacím prvku s křížkem.

Smyčka mainloop mezitím koná velice důležitou práci. Hlídá, jestli v souvisejícím prostředí nedošlo k nějaké události

Událostí může být pohyb kurzoru, stisk či uvolnění tlačítka myší nebo klávesnice, změna velikosti okna a také zaměření (focus). Je-li událost programově ošetřena (což v našem případě je implicitně také), procedura mainloop() to zaregistruje a uvědomí příslušný piškot (či proceduru), který (která) zařídí další - v našem případě zavře wokno.

Focus je stav aktivity, který umožňuje spojení widgetu s událostí klávesnice. V jednom okamžiku může mít focus jen jediný widget (vidíme kolem něho tečkovaný rámeček).

Přesun zaměření z jednoho widgetu na druhý lze provést několika způsoby:

klik levého tlačítka myši nad widgetem
najetí kurzoru nad widget
stisk tlačítka TAB, které způsobí procházení seznamem piškotů
Stisk mezerníku je událost, která spustí ten widget, na který ukazuje focus.
Spojení události s připravenou reakcí piškotu lze realizovat buď prostřednictvím parametru command (jen u některých piškotů) nebo metodou .bind().

Správa geometrie
Pozice jednotlivých piškotů a rámečků uvnitř nadřízených kontejnerů se určují pomocí správců geometrie, jež jsou tři:

packer - používá metodu   pack()
grider - používá metodu   grid()
placer - používá metodu   place()
Nejjednodušší je metoda pack, doporučovaná a nejvšestrannější je metoda grid.


A.5   Praktická ukázka II
Při programování grafických prvků se velmi často používají třídy. Ukážeme si trochu rozvinutou variantu předchozí ukázky (hello2.py):

 1  from tkinter import*
 2
 3  class Hello:
 4      def __init__(self, master):
 5          frame = Frame(master)
 6          frame.pack()
 7          self.button = Button(frame, text="QUIT", fg="red",
                                command=frame.quit)
 8          self.button.pack(side=LEFT)
 9          self.hi = Button(frame, text="Nazdar!",
                            command=self.say_hi)
10          self.hi.pack(side=LEFT)
11      def say_hi(self):
            print("Nazdárek Kašpárek")
12  root = Tk()
13  app = Hello(root)
14  root.mainloop()
C:\CodeTest\tk-py> python33 hello.py
Nazdárek Kašpárek
Vytvořili jsme okno se dvěma tlačítky. Jedním způsobíme tisk oslovení "Nazdárek Kašpárek" v okně konzoly, druhým okno zavřeme:


Jednotlivé řádky skriptu mají tento význam:

Na prvním řádku importujeme všechny objekty modulu tkinter.
---
Počátek deklarace vlastní třídy.
Konstruktor s povinným atributem self a vlastním atributem master, jímž bude instance root .
V rámci konstruktoru vytváříme instanci třídy Frame, která má jeden atribut, jímž má být název rodičovského objektu; v našem případě to bude "root".
Povinná expozice objektu frame.
Deklarace tlačítka jako instance třídy Button. Zástupné self naznačuje, že tlačítko bude vytvořeno pro instanci třídy "Hello". Parametry v závorce uvádějí jméno nadřízeného piškotu, text na tlačítku, barvu pozadí a jméno nativní funkce, která bude volaná při stisku tlačítka.
Povinná expozice objektu s parametrem side=LEFT, což znamená, že toto tlačítko se v nadřazeném piškotu "frame" umístí vlevo nahoru.
Deklarace dalšího tlačítka s názvem hi. Parametr command tentokrát uvádí jméno vlastní funkce, která bude volaná při stisku tlačítka.
Opět povinná expozice objektu.
Definice funkce say_hi, která při své evokaci vytiskne zadaný text.
Nejvýše postavené okno aplikace jako instance třídy Tk.
Vytvoření instance třídy Hello, která je nositelem deklarovaných piškotů a metod.
Evokace smyčky pro objekt root.
Při deklaraci tlačítek button a hi jsme využili implicitně přiřazenou událost <Button-1>, což je stisk levého tlačítka myši.

Projdeme-li skriptem od shora dolů, uvědomíme si, že kromě importu na prvním řádku začíná výpočet na řádku 12 vytvořením nejvýše postaveného okna root, které hned na řádku 13 použijeme jako argument při tvorbě instance třídy Hello.
Tento argument použije konstruktor třídy Hello jako hodnotu pro parametr master.

Nabízí se otázka, k čemu vlastně potřebujeme deklarovat piškot frame? Když upravíte hello2.py tak aby se v něm piškot frame nevyskytoval, zjistíte, že dostanete téměř shodné okno - pouze s tím rozdílem, že tlačítka QUIT a "Nazdar!" jsou posunutá až k okraji okna.
Piškot frame tedy zajistil jejich centrické umístění.

Více se dozvíte v navazujícím textu:   Tkinter Pythonu.


comment up  next    how to  end end

# ================================
miko oddel
# ================================
GNU Free Documentation License
# ================================

Version 1.1, March 2000
Copyright © 2000 Free Software Foundation, Inc.
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

Preamble
The purpose of this License is to make a manual, textbook, or other written document "free" in the sense of freedom: to assure everyone the effective freedom to copy and redistribute it, with or without modifying it, either commercially or noncommercially. Secondarily, this License preserves for the author and publisher a way to get credit for their work, while not being considered responsible for modifications made by others.

This License is a kind of "copyleft," which means that derivative works of the document must themselves be free in the same sense. It complements the GNU General Public License, which is a copyleft license designed for free software.

We have designed this License in order to use it for manuals for free software, because free software needs free documentation: a free program should come with manuals providing the same freedoms that the software does. But this License is not limited to software manuals; it can be used for any textual work, regardless of subject matter or whether it is published as a printed book. We recommend this License principally for works whose purpose is instruction or reference.

Applicability and Definitions
This License applies to any manual or other work that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. The "Document," below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you."

A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of the Document that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (For example, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical, or political position regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are designated, as being those of Invariant Sections, in the notice that says that the Document is released under this License.

The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the Document is released under this License.

A "Transparent" copy of the Document means a machine-readable copy, represented in a format whose specification is available to the general public, whose contents can be viewed and edited directly and straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup has been designed to thwart or discourage subsequent modification by readers is not Transparent. A copy that is not "Transparent" is called "Opaque."

Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML designed for human modification. Opaque formats include PostScript, PDF, proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML produced by some word processors for output purposes only.

The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.

Verbatim Copying
You may copy and distribute the Document in any medium, either commercially or noncommercially, provided that this License, the copyright notices, and the license notice saying this License applies to the Document are reproduced in all copies, and that you add no other conditions whatsoever to those of this License. You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute. However, you may accept compensation in exchange for copies. If you distribute a large enough number of copies you must also follow the conditions in Section 3.

You may also lend copies, under the same conditions stated above, and you may publicly display copies.

Copying in Quantity
If you publish printed copies of the Document numbering more than 100, and the Document's license notice requires Cover Texts, you must enclose the copies in covers that carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly and legibly identify you as the publisher of these copies. The front cover must present the full title with all words of the title equally prominent and visible. You may add other material on the covers in addition. Copying with changes limited to the covers, as long as they preserve the title of the Document and satisfy these conditions, can be treated as verbatim copying in other respects.

If the required texts for either cover are too voluminous to fit legibly, you should put the first ones listed (as many as fit reasonably) on the actual cover, and continue the rest onto adjacent pages.

If you publish or distribute Opaque copies of the Document numbering more than 100, you must either include a machine-readable Transparent copy along with each Opaque copy, or state in or with each Opaque copy a publicly accessible computer-network location containing a complete Transparent copy of the Document, free of added material, which the general network-using public has access to download anonymously at no charge using public-standard network protocols. If you use the latter option, you must take reasonably prudent steps, when you begin distribution of Opaque copies in quantity, to ensure that this Transparent copy will remain thus accessible at the stated location until at least one year after the last time you distribute an Opaque copy (directly or through your agents or retailers) of that edition to the public.

It is requested, but not required, that you contact the authors of the Document well before redistributing any large number of copies, to give them a chance to provide you with an updated version of the Document.

Modifications
You may copy and distribute a Modified Version of the Document under the conditions of Sections 2 and 3 above, provided that you release the Modified Version under precisely this License, with the Modified Version filling the role of the Document, thus licensing distribution and modification of the Modified Version to whoever possesses a copy of it. In addition, you must do these things in the Modified Version:

Use in the Title Page (and on the covers, if any) a title distinct from that of the Document, and from those of previous versions (which should, if there were any, be listed in the History section of the Document). You may use the same title as a previous version if the original publisher of that version gives permission.
List on the Title Page, as authors, one or more persons or entities responsible for authorship of the modifications in the Modified Version, together with at least five of the principal authors of the Document (all of its principal authors, if it has less than five).
State on the Title page the name of the publisher of the Modified Version, as the publisher.
Preserve all the copyright notices of the Document.
Add an appropriate copyright notice for your modifications adjacent to the other copyright notices.
Include, immediately after the copyright notices, a license notice giving the public permission to use the Modified Version under the terms of this License, in the form shown in the Addendum below.
Preserve in that license notice the full lists of Invariant Sections and required Cover Texts given in the Document's license notice.
Include an unaltered copy of this License.
Preserve the section entitled "History," and its title, and add to it an item stating at least the title, year, new authors, and publisher of the Modified Version as given on the Title Page. If there is no section entitled "History" in the Document, create one stating the title, year, authors, and publisher of the Document as given on its Title Page, then add an item describing the Modified Version as stated in the previous sentence.
Preserve the network location, if any, given in the Document for public access to a Transparent copy of the Document, and likewise the network locations given in the Document for previous versions it was based on. These may be placed in the "History" section. You may omit a network location for a work that was published at least four years before the Document itself, or if the original publisher of the version it refers to gives permission.
In any section entitled "Acknowledgements" or "Dedications," preserve the section's title, and preserve in the section all the substance and tone of each of the contributor acknowledgements and/or dedications given therein.
Preserve all the Invariant Sections of the Document, unaltered in their text and in their titles. Section numbers or the equivalent are not considered part of the section titles.
Delete any section entitled "Endorsements." Such a section may not be included in the Modified Version.
Do not retitle any existing section as "Endorsements" or to conflict in title with any Invariant Section.
If the Modified Version includes new front-matter sections or appendices that qualify as Secondary Sections and contain no material copied from the Document, you may at your option designate some or all of these sections as invariant. To do this, add their titles to the list of Invariant Sections in the Modified Version's license notice. These titles must be distinct from any other section titles. You may add a section entitled "Endorsements," provided it contains nothing but endorsements of your Modified Version by various parties     for example, statements of peer review or that the text has been approved by an organization as the authoritative definition of a standard. You may add a passage of up to five words as a Front-Cover Text, and a passage of up to 25 words as a Back-Cover Text, to the end of the list of Cover Texts in the Modified Version. Only one passage of Front-Cover Text and one of Back-Cover Text may be added by (or through arrangements made by) any one entity. If the Document already includes a cover text for the same cover, previously added by you or by arrangement made by the same entity you are acting on behalf of, you may not add another; but you may replace the old one, on explicit permission from the previous publisher that added the old one. The author(s) and publisher(s) of the Document do not by this License give permission to use their names for publicity for or to assert or imply endorsement of any Modified Version.
Combining Documents
You may combine the Document with other documents released under this License, under the terms defined in Section 4 above for modified versions, provided that you include in the combination all of the Invariant Sections of all of the original documents, unmodified, and list them all as Invariant Sections of your combined work in its license notice. The combined work need only contain one copy of this License, and multiple identical Invariant Sections may be replaced with a single copy. If there are multiple Invariant Sections with the same name but different contents, make the title of each such section unique by adding at the end of it, in parentheses, the name of the original author or publisher of that section if known, or else a unique number. Make the same adjustment to the section titles in the list of Invariant Sections in the license notice of the combined work. In the combination, you must combine any sections entitled "History" in the various original documents, forming one section entitled "History"; likewise combine any sections entitled "Acknowledgements," and any sections entitled "Dedications." You must delete all sections entitled "Endorsements."
Collections of Documents
You may make a collection consisting of the Document and other documents released under this License, and replace the individual copies of this License in the various documents with a single copy that is included in the collection, provided that you follow the rules of this License for verbatim copying of each of the documents in all other respects. You may extract a single document from such a collection, and distribute it individually under this License, provided you insert a copy of this License into the extracted document, and follow this License in all other respects regarding verbatim copying of that document.
Aggregation with Independent Works
A compilation of the Document or its derivatives with other separate and independent documents or works, in or on a volume of a storage or distribution medium, does not as a whole count as a Modified Version of the Document, provided no compilation copyright is claimed for the compilation. Such a compilation is called an "aggregate," and this License does not apply to the other self-contained works thus compiled with the Document, on account of their being thus compiled, if they are not themselves derivative works of the Document.
If the Cover Text requirement of Section 3 is applicable to these copies of the Document, then if the Document is less than one quarter of the entire aggregate, the Document's Cover Texts may be placed on covers that surround only the Document within the aggregate. Otherwise they must appear on covers around the whole aggregate.

Translation
Translation is considered a kind of modification, so you may distribute translations of the Document under the terms of Section 4. Replacing Invariant Sections with translations requires special permission from their copyright holders, but you may include translations of some or all Invariant Sections in addition to the original versions of these Invariant Sections. You may include a translation of this License provided that you also include the original English version of this License. In case of a disagreement between the translation and the original English version of this License, the original English version will prevail.

Termination
You may not copy, modify, sublicense, or distribute the Document except as expressly provided for under this License. Any other attempt to copy, modify, sublicense, or distribute the Document is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.

Future Revisions of This License
The Free Software Foundation may publish new, revised versions of the GNU Free Documentation License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. See http:///www.gnu.org/copyleft/.

Each version of the License is given a distinguishing version number. If the Document specifies that a particular numbered version of this License "or any later version" applies to it, you have the option of following the terms and conditions either of that specified version or of any later version that has been published (not as a draft) by the Free Software Foundation. If the Document does not specify a version number of this License, you may choose any version ever published (not as a draft) by the Free Software Foundation.

Addendum: How to Use This License for Your Documents
To use this License in a document you have written, include a copy of the License in the document and put the following copyright and license notices just after the title page:

Copyright © YEAR YOUR NAME. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with the Invariant Sections being LIST THEIR TITLES, with the Front-Cover Texts being LIST, and with the Back-Cover Texts being LIST. A copy of the license is included in the section entitled "GNU Free Documentation License."
If you have no Invariant Sections, write "with no Invariant Sections" instead of saying which ones are invariant. If you have no Front-Cover Texts, write "no Front-Cover Texts" instead of "Front-Cover Texts being LIST"; likewise for Back-Cover Texts.

If your document contains nontrivial examples of program code, we recommend releasing these examples in parallel under your choice of free software license, such as the GNU General Public License, to permit their use in free software.

previous    up  end hi  end end

