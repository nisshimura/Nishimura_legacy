public abstract class Person {
    private String name;
    private int possesion;

    public Person(String name,int possesion){
        this.name = name;
        this.possesion = possesion;
    }

    String getName(){
        return this.name;
    }
    int getMoney(){
        return this.possesion;
    }
    void changeMoney(int out){
        this.possesion -= out;
    }
    void print(){
        System.out.println(this.name + " now has "+this.possesion+" yen");
    }
    abstract int getFee();
}

