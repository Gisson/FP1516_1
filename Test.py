#$File created by Jorge Heleno
#October the 19th 02:07
#Please do not change anything in this file
#File under the GPL license

import unittest;
#Trocar "main" pelo nome do ficheiro com o projecto
from main import *;

class AdvancedOperation(unittest.TestCase):
    testTuple=('a','A',' ','.',',',';','B','C','D','d','o','P');

    def test_Generate(self):
        print("Advanced Generate test Running");
        self.assertEqual(gera_chave2(self.testTuple),(('a','A',' '),('.',',',';'),('B','C','D'),('d','o','P')),"Error in gera_chave2");

    def test_getCode1(self):
        print("Advanced getCode1 test running");
        self.assertEqual(obtem_codigo1('a',gera_chave2(self.testTuple)),'00',"Erro on obtem-codigo2");
    def test_getCode2(self):
        print("Advanced getCode2 test running");
        self.assertEqual(obtem_codigo2('o',gera_chave2(self.testTuple)),'31',"Erro on obtem-codigo2");
    def test_getCode3(self):
        print("Advanced getCode3 test running");
        self.assertEqual(obtem_codigo2('+',gera_chave2(self.testTuple)),'XX',"Erro on obtem-codigo2");

    def test_codify1(self):
        print("Advanced codify1 test running");
        self.assertEqual(codifica2('BCa.oP',gera_chave2(self.testTuple)),'202100103132',"Erro on codifica2");

    def test_codify2(self):
        print("Advanced codify2 test running");
        self.assertEqual(codifica2('ddd',gera_chave2(self.testTuple)),'303030',"Erro on codifica2");
    def test_codify3(self):
        print("Advanced codify3 test running");
        self.assertEqual(codifica2(',AhxlPITYxpw;vqiFMLQcrQmFocNmxRtLRKHyHjaVVJeIKWvyZSpezKlUadjAREODhByOdwZVHepqCZwIQ;ChITNgHKcEHWuJDqqF,YzJCwO,CyvOGntEJpxKcJxYouMGxrRVCITlebhC,clqJKLnTTV;mMWHorYtUCU;SzEBMTxJLyNmBIintILyWuwfXnWJxTlTnOdmjAiMSNNDSLXqHyadPiJknVJsNDhVfQhuSHUGcgTrh;VwrBrxze;vCxDTgrqEvnT,DYzoJShRiIWTEAWL;DfRUSNRRRDlpYRMedKcw;YKzfdCZMRyoToOepfQJQAwfMAXKyIDfKnaFetKQSaxnmtLwqZUm;hZyjaQeZZmEzm,CwtEVQoNPGoQqujoLlcQACeOFrZctiQk,SbpRcHWfHVZH,wRSnMsSkXa,tbQKWKoDZhwBsNvclqSoByUhMKfgdOdqjNVIDzUApuRlUbSMPgsUjJYHyukjeIFxfrcgkMXvJB',gera_chave2(self.testTuple)),'1101XXXXXX32XXXXXXXXXXXX12XXXXXXXXXXXXXXXXXXXXXXXX31XXXXXXXXXXXXXXXXXXXXXXXXXX00XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0030XX01XXXXXX22XX20XXXX30XXXXXXXXXXXXXX21XXXXXXXX1221XXXXXXXXXXXXXXXXXXXXXXXXXX22XXXXXX11XXXXXX21XXXX1121XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX31XXXXXXXXXXXXXX21XXXXXXXXXXXX2111XXXXXXXXXXXXXXXXXXXX12XXXXXXXX31XXXXXXXX21XX12XXXXXX20XXXXXXXXXXXXXXXX20XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX30XXXX01XXXXXXXXXX22XXXXXXXXXXXX003032XXXXXXXXXXXXXXXX22XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX12XXXXXX20XXXXXXXX12XX21XX22XXXXXXXXXXXXXXXX1122XXXX31XXXXXXXXXXXXXXXXXX01XXXX1222XXXXXXXXXXXXXXXX22XXXXXXXXXXXX30XXXXXX12XXXXXXXX3021XXXXXXXX31XX31XXXXXXXXXXXXXX01XXXXXX01XXXXXXXX22XXXXXX00XXXXXXXXXXXX00XXXXXXXXXXXXXXXXXXXX12XXXXXXXX00XXXXXXXXXXXXXXXX1121XXXXXXXXXX31XX32XX31XXXXXXXX31XXXXXXXX0121XXXXXXXXXXXXXXXXXXXX11XXXXXXXXXXXXXXXXXXXXXXXX11XXXXXXXXXXXXXXXXXX0011XXXXXXXXXXXX3122XXXXXX20XXXXXXXXXXXXXX3120XXXXXXXXXXXXXX30XX30XXXXXXXXXX22XXXX01XXXXXXXXXXXXXXXX32XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX20',"Erro on codifica2");
    def test_getCar1(self):
        print("Advanced getCar1 test running");
        self.assertEqual(obtem_car2('00',gera_chave2(self.testTuple)),'a',"Erro on obtem_car2");
    def test_getCar2(self):
        print("Advanced getCar2 test running");
        self.assertEqual(obtem_car2('31',gera_chave2(self.testTuple)),'o',"Erro on obtem_car2");
    def test_getCar3(self):
        print("Advanced getCar3 test running");
        self.assertEqual(obtem_car2('XX',gera_chave2(self.testTuple)),'?',"Erro on obtem_car2");
    def test_decrypt(self):
        print("Advanced decrypt test running");
        self.assertEqual(descodifica2('11003030XX3011301121XX2210XX10XX22XX1011122130XXXX101212221020XX22XX11XXXXXX00003001XX2030200111XX300100300122121210XX1211XXXX112030XX1230300000101000XX2211XX21001230XX10XX001000223021XX2222XX20112221XXXX2211XX12XXXX10XX2111121201XX00XX00111111XX101001212101013030102211002212XX110012102120102211XXXX212200102130XX21300022202122XX1211XX1211102001120010XXXXXX102011202030XXXXXX1020XX211201211121XX12120021213001XX20202222XX00XX0110XX20102200100011XXXX1211XXXX01201221221230101200XX1110XXXX01XXXX12XX121212XXXX1000XX12XX0001110012XX120000XX11122222302101XX21XX102210102100120101122100XX200001122120110130XX102111201120XX30000111002010XX0101201212XX00XX222030XX22002012XX20000030003001110000202101XXXX2030XX10XXXX2011XX11XX2030202200XXXX20XX22222001XX202210112211102230012011XX120012XXXX2120221012XXXX2001XX00XX010121XX22211211113011XX2130212110223000XX002110203021XX211111220121211022XXXX11213030102010XX0112XX1112001122XX12012222211200XX30302112220022XX22XX122021121000113012XX10212212XX103030XXXXXXXX',gera_chave2(self.testTuple)),',add?d,d,C?D.?.?D?.,;Cd??.;;D.B?D?,???aadA?BdBA,?dAadAD;;.?;,??,Bd?;ddaa..a?D,?Ca;d?.?a.aDdC?DD?B,DC??D,?;??.?C,;;A?a?a,,,?..ACCAAdd.D,aD;?,a;.CB.D,??CDa.Cd?CdaDBCD?;,?;,.BA;a.???.B,BBd???.B?C;AC,C?;;aCCdA?BBDD?a?A.?B.Da.a,??;,??AB;CD;d.;a?,.??A??;?;;;??.a?;?aA,a;?;aa?,;DDdCA?C?.D..Ca;AA;Ca?BaA;CB,Ad?.C,B,B?daA,aB.?AAB;;?a?DBd?DaB;?BaadadA,aaBCA??Bd?.??B,?,?BdBDa??B?DDBA?BD.,D,.DdAB,?;a;??CBD.;??BA?a?AAC?DC;,,d,?CdCC.Dda?aC.BdC?C,,DACC.D??,Cdd.B.?A;?,;a,D?;ADDC;a?ddC;DaD?D?;BC;.a,d;?.CD;?.dd????',"Erro on descodifica1");





class NormalOperation(unittest.TestCase):
    testTuple=('a','A',' ','.',',',';','B','C','D','d','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=');

    def test_Generate(self):
        print("Generate test Running");
        self.assertEqual(gera_chave1(self.testTuple),(('a','A',' ','.',','),(';','B','C','D','d'),('=','=','=','=','='),('=','=','=','=','='),('=','=','=','=','=')),"Error in gera_chave");
    def test_getCode1(self):
        print("getCode1 test running");
        self.assertEqual(obtem_codigo1('a',gera_chave1(self.testTuple)),'00',"Erro on obtem-codigo1");
    def test_getCode2(self):
        print("getCode2 test running");
        self.assertEqual(obtem_codigo1(';',gera_chave1(self.testTuple)),'10',"Erro on obtem-codigo1");

    def test_getCode3(self):
        print("getCode3 test running");
        self.assertEqual(obtem_codigo1('d',gera_chave1(self.testTuple)),'14',"Erro on obtem-codigo1");
    def test_codify1(self):
        print("codify1 test running");
        self.assertEqual(codifica1('BCa.',gera_chave1(self.testTuple)),'11120003',"Erro on codifica1");

    def test_codify2(self):
        print("codify2 test running");
        self.assertEqual(codifica1('ddd',gera_chave1(self.testTuple)),'141414',"Erro on codifica1");

    def test_getCar1(self):
        print("getCar1 test running");
        self.assertEqual(obtem_car1('00',gera_chave1(self.testTuple)),'a',"Erro on obtem_car1");
    def test_getCar2(self):
        print("getCar2 test running");
        self.assertEqual(obtem_car1('14',gera_chave1(self.testTuple)),'d',"Erro on obtem_car1");
    def test_getCar3(self):
        print("getCar3 test running");
        self.assertEqual(obtem_car1('11',gera_chave1(self.testTuple)),'B',"Erro on obtem_car1");
    def test_decrypt(self):
        print("decrypt test running");
        self.assertEqual(descodifica1('120014',gera_chave1(self.testTuple)),'Cad',"Erro on descodifica1");



if __name__ == '__main__':
    unittest.main()
