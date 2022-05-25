public class Adult extends Person {
    public Adult(String name,int possesion){
        super(name,possesion);
    }
    int getFee() {
        return 200;
    }
}