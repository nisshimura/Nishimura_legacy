import java.util.*;

public class funi_second {
    static final String[] ORDERS = {"ac", "af", "dc", "df", "sc", "sf", "return", "close"};
    static List<String> FUNITURES = new ArrayList<String>(Arrays.asList("chair", "table", "pot"));

    static List<List<Integer>> funis_youhave = new ArrayList<List<Integer>>();// FUNITURES
    static int[][] tmp_num_funis = {{10, 0}, {9, 0}, {6, 0}};// remaining/rented

    static int nowID = 0;
    static List<List<String>> cus_funi_list = new ArrayList<List<String>>();// {{"Bob","0","chair","chair"},{"Tom","1","chair,"pot"}}

    public void add_cus(String name) {
        List<String> tmp = new ArrayList<String>();
        tmp.add(name);
        tmp.add(String.valueOf(nowID++));
        cus_funi_list.add(tmp);
    }

    public static List<List<Integer>> array2list(int[][] array) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        for (int i = 0; i < array.length; i++) {
            List<Integer> tmp = new ArrayList<Integer>();
            for (int j = 0; j < array[i].length; j++)
                tmp.add(array[i][j]);
            list.add(tmp);
        }
        return list;
    }

    public boolean rental_funi(String name, String funi) {
        if (!isInCusList(name)){
            System.out.println("You are not member!\nPlz become member!");
            return false;
        }

        if (calc_num_funis(funi, true))
            cus_funi_list.get(select_person(name)).add(funi);
        return true;
    }

    public boolean del_cus(String name) {
        if (!isInCusList(name)) {
            System.out.println("You are not member!");
            return false;
        }
        int index = select_person(name);
        for (int i = 1; i < cus_funi_list.get(index).size(); i++)
            calc_num_funis(cus_funi_list.get(index).get(i), false);
        cus_funi_list.remove(index);
        return true;
    }

    public int count_funi(int id,String funi) {
        int count = 0;
        for (int i = 0; i < cus_funi_list.get(indexOfCusList(name)).size(); i++)
            if (cus_funi_list.get(indexOfCusList(name)).get(i).equals(funi))
                count++;
        return count;
    }

    public boolean calc_num_funis(String funi, boolean isRental) {
        if (!isYouHaveStock(funi))
            return false;
        if (isRental) {
            funis_youhave.get(FUNITURES.indexOf(funi)).set(0,
                    funis_youhave.get(FUNITURES.indexOf(funi)).get(0) - 1);
            funis_youhave.get(FUNITURES.indexOf(funi)).set(1,
                    funis_youhave.get(FUNITURES.indexOf(funi)).get(1) + 1);
        } else {
            funis_youhave.get(FUNITURES.indexOf(funi)).set(0,
                    funis_youhave.get(FUNITURES.indexOf(funi)).get(0) + 1);
            funis_youhave.get(FUNITURES.indexOf(funi)).set(1,
                    funis_youhave.get(FUNITURES.indexOf(funi)).get(1) - 1);
        }
        return true;
    }

    public int select_person(String name){
        List<Integer> p = indexOfCusList(name);
        String str;
        if (p.size() == 1)
            return 0;
        else {
            System.out.println(name + " is used by " + Integer.valueOf(p.size()) + " people");
            print_sf();
            System.out.print("Plz select index 0 to "+Integer.valueOf(p.size())+" : ");
            Scanner scan = new Scanner(System.in);
            str = scan.nextLine();
        }
        return p.get(Integer.valueOf(str));
    }
    public void print_sf(){
        String formatter1 = "%7s%-15s%-15s%n";
        System.out.printf(formatter1, "index","funi_name", "remain/rented");
        for (int i = 0; i < funis_youhave.size(); i++)
            System.out.printf(formatter1, Integer.valueOf(i),FUNITURES.get(i),String.valueOf(funis_youhave.get(i).get(0)) + "/"+ String.valueOf(funis_youhave.get(i).get(1)));
    }

    public void print_sc(){
        System.out.printf("%7s%-15s","index","name");
        for (int i = 0; i < FUNITURES.size(); i++)
            System.out.printf("%10s", FUNITURES.get(i));
        System.out.printf("%n");

        for (int i = 0; i < cus_funi_list.size(); i++) {
            String name = cus_funi_list.get(i).get(0);
            System.out.printf("%7s", i);
            System.out.printf("%15s", name);
            for (int j = 0; j < FUNITURES.size(); j++)
                System.out.printf("%10s",count_funi(cus_funi_list.get(i).get(0), FUNITURES.get(j)));
            System.out.printf("%n");
        }
    }

    public boolean isYouHaveStock(String funi) {
        boolean flag = funis_youhave.get(FUNITURES.indexOf(funi)).get(0) > 0;
        if (!flag)
            System.out.println(funi + " is out of order");
        return flag;
    }

    public void return_funi(String name, String funi) {
        cus_funi_list.get(indexOfCusList(name))
                .remove(cus_funi_list.get(indexOfCusList(name)).indexOf(funi));
        calc_num_funis(funi, false);
    }

    public List<Integer> indexOfCusList(String name) {
        List<Integer> num = new ArrayList<Integer>();
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(0).equals(name))
                num.add(i);
        return num;
    }
    
    public int indexOfCusList_id(int id) {
        int num = 0;
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(0).equals(name))
                num=i;
        return num;
    }

    public boolean isInCusList(String name) {
        boolean flag = false;
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(0).equals(name))
                flag = true;
        return flag;
    }

    public boolean isAvailableOrder(String order) {
        boolean flag = false;
        for (int i = 0; i < ORDERS.length; i++)
            if (order.equals(ORDERS[i]))
                flag = true;
        if (!flag)
            System.out.println(order + ", This Order is not AVAILABLE");
        return flag;
    }

    public boolean isAvailableFuni(String funi) {
        boolean flag = false;
        for (int i = 0; i < FUNITURES.size(); i++)
            if (funi.equals(FUNITURES.get(i)))
                flag = true;
        if (!flag)
            System.out.println(funi + " is not AVAILABLE");
        return flag;
    }

    public static void main(String[] args) {


        funi_second a = new funi_second();
        funis_youhave = array2list(tmp_num_funis);

        for (;;) {
            Scanner scan = new Scanner(System.in);
            System.out.println("Enter admin/customer");
            String str = scan.nextLine();
            if (!(str.equals("admin") || str.equals("customer")))
                continue;
            boolean isAdmin = str.equals("admin");
            if (isAdmin) {// Administrator
                for (;;) {
                    System.out.println("Enter Your Order: ");
                    System.out.println("ADD Customer : ac");
                    System.out.println("ADD Furniture : af");

                    System.out.println("Delete Customer : dc");
                    System.out.println("Delete Furniture : df");

                    System.out.println("Show Num Of Funitures (remaining/rented): sf");
                    System.out.println("Show ALL Customers Information: sc");

                    System.out.println("Return : return");
                    System.out.println("Close : close");

                    String order = scan.nextLine();
                    if (!a.isAvailableOrder(order))
                        continue;
                    if (order.equals("return"))
                        break;
                    switch (order) {
                        case "ac":
                            // ADD Customer
                            System.out.println(
                                    "Enter New Customers you need to add (Plz split with ,)");
                            String name1 = scan.nextLine();
                            String[] names1 = name1.split(",");
                            for (int i = 0; i < names1.length; i++)
                                a.add_cus(names1[i]);
                            break;
                        case "af":
                            // ADD Funiture
                            System.out.println(
                                    "Enter Target Customer you need to add (OK to new one)");
                            String name2 = scan.nextLine();
                            System.out.println("Enter Funitures you need rent (Plz split with ,)");
                            String funi2 = scan.nextLine();
                            String[] funis2 = funi2.split(",");
                            for (int i = 0; i < funis2.length; i++)
                                if (a.isAvailableFuni(funis2[i]))
                                    a.rental_funi(name2, funis2[i]);
                            break;
                        case "dc":
                            // DELETE Customers
                            System.out.println(
                                    "Enter customers you need to DELETE (Plz split with ,)");
                            String name3 = scan.nextLine();
                            String[] names3 = name3.split(",");
                            for (int i = 0; i < names3.length; i++)
                                a.del_cus(names3[i]);
                            break;
                        case "df":
                            // DELETE Funitures
                            System.out.println("Enter Target Customer you need to DELETE");
                            String name4 = scan.nextLine();
                            System.out.println("Enter Funitures you need DELETE (Plz split with ,)");
                            String funi4 = scan.nextLine();
                            String[] funis4 = funi4.split(",");
                            for (int i = 0; i < funis4.length; i++)
                                if (a.isAvailableFuni(funis4[i]))
                                    a.return_funi(name4, funis4[i]);
                            break;
                        case "sf":
                            a.print_sf();
                            break;
                        case "sc":
                            a.print_sc();
                            break;
                        case "close":
                            System.out.println("See you!!");
                            System.exit(1);
                    }
                }
            } else {
                System.out.println("Enter new/member");

            }
            System.out.println(cus_funi_list);
        }
    }
}
