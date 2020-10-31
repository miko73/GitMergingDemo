
============================================================================== 
miko odkazy


miko c++ a C KB
https://www.tutorialspoint.com/cplusplus/cpp_quick_guide.htm
https://www.tutorialspoint.com/cplusplus/index.htm
https://www.sallyx.org/
https://medium.com/



miko git
https://blog.horejsek.com/jasne-umim-git-dot-dot-dot/

miko codity
https://programming-review.com/python/algorithms#primes

miko kurzy
https://www.itnetwork.cz/cplusplus/zaklady/c-plus-plus-tutorial-visual-studio-a-prvni-konzolova-aplikace

miko ladeni
miko valgrind
http://jaknaprojekty.davidm.cz/ladeni-valgrind.html

==================
power shell
https://social.technet.microsoft.com/wiki/contents/articles/2969.windows-powershell-ise-add-on-tools.aspx#SeeAlso


============================================================================== 
hello world

#include <iostream>
using namespace std;

int main(void)
{
    cout << "Hello world!" << endl;
    cin.get();
    return 0;
}
============================================================================== 
miko konstaty miko const
#include <iostream>
using namespace std;

#define LENGTH 10   
#define WIDTH  5
#define NEWLINE '\n'

int main() {
   int area;  
   
   area = LENGTH * WIDTH;
   cout << area;
   cout << NEWLINE;
   return 0;
}



#include <iostream>
using namespace std;

int main() {
   const int  LENGTH = 10;
   const int  WIDTH  = 5;
   const char NEWLINE = '\n';
   int area;  
   
   area = LENGTH * WIDTH;
   cout << area;
   cout << NEWLINE;
   return 0;
}
============================================================================== 
using namespace std;

int main(void)
{
    cout << "Ahoj, jsem virtualni papousek Lora, rad opakuji!" << endl;
    cout << "Napis neco: " << endl;
    string vstup;
    cin >> vstup;
    string vystup;
    vystup = vstup + ", " + vstup + "!";
    cout << vystup << endl;
    cin.get(); cin.get();
    return 0;
}
============================================================================== 
Secure Boot disabled.
enable secure boot
enable UEFI and Secure Boot and then restart 


============================================================================== 
miko array alokace
Díky závorkám C++ ví, že má mazat pole. 
Je také duležité, aby typ ukazatele byl stejný jako typ uložených dat (protože ukazatele mužeme pretypovat). 
Pokud zmeníte typ ukazatele a potom se jej pokusíte odstranit, bude výsledek nejistý a program muže spadnout 
nebo uvolnit špatnou velikost pameti. 
V každém prípade se program dostane do situace, která by v žádném prípade nemela nastat.

int* pole = new int[10];
pole[5] = 125;

delete [] pole;
============================================================================== 
#include <iostream>
#include <string>
using namespace std;
int main()
{
// Alokace 100 intu
    int *pole = new int[100];
    if( pole == NULL )
    {
        cout << "Nedostatek pameti." << endl;
        return 1;
    }

// Výpocet adresy pátého prvku
    int *paty_prvek = pole + 4;

// Uložení hodnoty na pátý prvek
    *paty_prvek = 56;

// Uvolnení pameti
    delete[] pole;
    pole = NULL;
}

============================================================================== 
#include <iostream>
using namespace std;

int main( ) {
    cout << "Zadej pocet znamek: ";
    int pocet;
    cin >> pocet;
    // Alokace bloku s daným poctem intu
    int* data = new int[pocet];
    if( data == NULL )
    {
        cout << "Nedostatek pameti" << endl;
        return 1;
    }
    // Postupné nactení známek do pole
    for(int* pozice = data; pozice < data + pocet; pozice++ )
    {
        cout << "Zadejte znamku: ";
        cin >> *pozice;
    }
    // Výpocet prumeru ze známek
    int soucet = 0;
    for(int* pozice = data; pozice < data + pocet; pozice++ )
    {
        soucet += *pozice;
        cout << *pozice << "\n";
    }
    double prumer = (double)soucet / pocet;
    cout << "Prumer tvych znamek je " << prumer << endl;
    // Uvolnení pameti
    delete[] data;
    data = NULL;
    cin.get(); cin.get();
    return 0;
}
============================================================================== 
#include <stdio.h>

int main(void)
{

    float pole[] = { 5.0, 6.0, 7.0, 8.0, 9.0 };
    float *ukazatel;

    ukazatel = pole;

    /* prvni cast */
    printf("%.1f ", pole[1]);
    printf("%.1f ", pole[1] + 10.0);
    printf("%.1f\n", (pole + 1)[2]);

    /* druha cast */
    printf("%.1f ", *ukazatel);
    printf("%.1f ", *ukazatel + 10);
    printf("%.1f ", *(ukazatel + 1));
    printf("%.1f\n", *(ukazatel + 1) + 10);

    return 0;
}

============================================================================== 
miko namespace
#include <iostream>

using namespace std;

namespace A
{
  int x = 5;
  void printX()
  {
    // function statements goes here
    cout<<x<<endl;
  }
}

namespace B
{
  int x=10;
  void printX()
  {
    // function statementsgoes here
    cout<<x<<endl;
  }
}

int main()
{
   A::printX() ;
   B::printX();
   
   return 0;
}
============================================================================== 

