public class Bus extends Car{
    public Person[] passengers;
    int nowNum =0;
    int Maxnum = 0;
    public Bus(int Maxnum){
        this.passengers = new Person[Maxnum];
        this.Maxnum = Maxnum;
    }
    public int getBusNum(){
        return super.num;
    }
    public void getOn(Person person){
        String name = person.getName();
        int fee = person.getFee();
        if (person.getMoney()<fee){
            System.out.println(name+" could not get on the bus");
        }
        else if (this.nowNum>=this.Maxnum){
            System.out.println(name + " could not get on the bus");
        }
        else{
            this.passengers[this.nowNum] = person;
            person.print();
            this.nowNum += 1;
        }
    }
    public void getOff(Person person){
        int flag=0;
        for (int i=0;i<this.nowNum;i++){
            if (this.passengers[i]==person){
                System.out.println(person.getName()+" got off the bus");
                flag = 1;
            }
        }
        if (flag==1){
            System.out.println(person.getName() + " was not on the bus");
        }
    }
    public void printAllPassengers(){
        for (int i = 0; i < this.nowNum; i++) {
            System.out.println(i + ":" +this.passengers[i].getName());
        }
    }
    public void printTotalFee(){
        int feeSum = 0;
        for (int i = 0; i < this.nowNum; i++) {
            feeSum += this.passengers[i].getFee();
        }
        System.out.println("feeSum"+feeSum);
    }
}
