#include <iostream>
#include <random>
using namespace std;
int main(){
 random_device rd;
 mt19937 gen(rd());
 uniform_real_distribution<float> distrib(0.0, 12.0);
 float coor1 = distrib(gen), coor2= distrib(gen), usimp1,usimp2;
 string name;
 int end;
 cout <<"Please, your name? ";
 cin >> name;
 cout<<"Welcome, "<< name <<", To : Save your girl/boy'."<<endl;
 cout<<"Your girlfriend/boyfriend was kidnapped by an zombie. You must rescue her/him, killing the zombie. you've only 3 shots."<<endl<<"Zombie's position equals to an point in the cartesian plan. (DECIMALS included)."<<endl;
   if (name!="Bianca"){
      end=3;}
   else{
      end=7;}
 for(int tries=1; tries<=(end);tries++)
   {cout<<"Input coordinate x: "; 
     cin>>usimp1;
     cout<<"Input coordinate y: "; 
     cin>>usimp2;
     if (((coor1 - usimp1) + (coor2 - usimp2))<=0.01) {
	    cout<<"Congrats,"<<name<<" ! Bull's eye on "<<tries<<"º shot/! Now, she/he's out of danger.";
	    return 0;}
     else{
      cout<<"It didn't, sorry. Precision of "<<(100*(usimp1/coor1))<<" % on x coordinate and "<<(100*(usimp2/coor2))<<" % on y coordinate. Try again."<<endl;}
      cout<<" If precision is bigger than 100%, its the excess"<<endl;
     if (((coor1-usimp1) + (coor2-usimp2))>0.01 && (tries==end)){
      cout<<"Well... Quite unfortunate, it's all over... \n The x value was: "<< coor1<<"\n And the y coord was: "<<coor2<<endl;}}
  return 0;}
