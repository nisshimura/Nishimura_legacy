import java.util.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import javax.lang.model.util.ElementScanner6;
public class funi_second {
    static List<String> FUNITURES = new ArrayList<String>();
    static List<List<Integer>> funis_youhave = new ArrayList<List<Integer>>();// FUNITURES
    static int nowID;
    static List<List<String>> cus_funi_list = new ArrayList<List<String>>();// {{"Bob","0","chair","chair"},{"Tom","1","chair,"pot"}}

    public funi_second() {
        String [] tmp_line;
        try {
			Path path = Paths.get("user_data.txt");
			List<String> lines = Files.readAllLines(path);
			
			for (int i=0;i<lines.size();i++) {
			    String str = lines.get(i); 
                tmp_line = str.split(",");
                List<String> tmp = new ArrayList<String>();
                if (i==0)
                    nowID = Integer.valueOf(tmp_line[0]);
                else{
                    for (int j=0;j<tmp_line.length;j++)   
                        tmp.add(tmp_line[j]);
                    cus_funi_list.add(tmp);
                }
			}
		} catch(IOException ioex) {
			ioex.printStackTrace();
		}

        try {
			Path path = Paths.get("funis_data.txt");
			List<String> lines = Files.readAllLines(path);
			
			for (int i=0;i<lines.size();i++) {
			    String str = lines.get(i); 
                tmp_line = str.split(",");
                FUNITURES.add(tmp_line[0]);
                List<Integer> tmp = new ArrayList<Integer>();
                tmp.add(Integer.valueOf(tmp_line[1]));
                tmp.add(Integer.valueOf(tmp_line[2]));
                funis_youhave.add(tmp);
			}
		} catch(IOException ioex) {
			ioex.printStackTrace();
		}
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

    public int select_person(String name) {
        List<Integer> p = indexOfCusList(name);
        String str;
        if (p.size() == 1)
            return p.get(0);
        else {
            System.out.println(name + " is used by " + Integer.valueOf(p.size()) + " people");
            print_by_name(name);
            System.out.print("Plz select index 0 to " + Integer.valueOf(p.size() - 1) + " : ");
            Scanner scan = new Scanner(System.in);
            str = scan.nextLine();
        }
        int idx = p.get(Integer.valueOf(str));
        return idx;
    }
    public void print_sf() {
        String formatter1 = "%-7s%-15s%-15s%n";
        System.out.printf(formatter1, "index", "funi_name", "remain/rented");
        for (int i = 0; i < funis_youhave.size(); i++)
            System.out.printf(formatter1, Integer.valueOf(i), FUNITURES.get(i),
                String.valueOf(funis_youhave.get(i).get(0)) + "/" + String.valueOf(funis_youhave.get(i).get(1)));
    }

    public void print_by_name(String name) {
        if (cus_funi_list.size()>0){
            List<Integer> p = indexOfCusList(name);

            System.out.printf("%-7s%-15s%-5s", "index", "name", "id");
            for (int i = 0; i < FUNITURES.size(); i++)
                System.out.printf("%-10s", FUNITURES.get(i));
            System.out.printf("%n");

            for (int i = 0; i < p.size(); i++) {
                String id = cus_funi_list.get(p.get(i)).get(1);
                System.out.printf("%-7s", i);
                System.out.printf("%-15s", name);
                System.out.printf("%-5s", id);
                for (int j = 0; j < FUNITURES.size(); j++)
                    System.out.printf("%-10s", count_funi(id, FUNITURES.get(j)));
                System.out.printf("%n");
            }
        }
        else
            System.out.println("There is no customer");
    }
    public void print_by_id(String id){
        int idx = indexOfCusList_id(id);
        if (cus_funi_list.get(idx).size()>2){
            System.out.printf("%-15s%-5s", "name", "id");
            for (int i = 0; i < FUNITURES.size(); i++)
                System.out.printf("%-10s", FUNITURES.get(i));
            System.out.printf("%n");

            System.out.printf("%-15s", cus_funi_list.get(idx).get(0));
            System.out.printf("%-5s", id);
            for (int j = 0; j < FUNITURES.size(); j++)
                System.out.printf("%-10s", count_funi(id, FUNITURES.get(j)));
            System.out.printf("%n");
        }
        else
            System.out.println("There is no RENTED things");
    }
    public void print_sc() {
        if (cus_funi_list.size()>0){
            System.out.printf("%-7s%-15s%-5s", "index", "name", "id");
            for (int i = 0; i < FUNITURES.size(); i++)
                System.out.printf("%-10s", FUNITURES.get(i));
            System.out.printf("%n");

            for (int i = 0; i < cus_funi_list.size(); i++) {
                List<String> tmp = cus_funi_list.get(i);
                String name = tmp.get(0);
                String id = tmp.get(1);
                System.out.printf("%-7s", i);
                System.out.printf("%-15s", name);
                System.out.printf("%-5s", id);
                for (int j = 0; j < FUNITURES.size(); j++)
                    System.out.printf("%-10s", count_funi(id, FUNITURES.get(j)));
                System.out.printf("%n");
            }
        }
        else
            System.out.println("There is no customer");
    }

    public boolean isYouHaveStock(String funi) {
        boolean flag = funis_youhave.get(FUNITURES.indexOf(funi)).get(0) > 0;
        if (!flag)
            System.out.println(funi + " is out of order");
        return flag;
    }

    public boolean isHavetargetfuni(String id, String funi) {
        int idx = indexOfCusList_id(id);
        boolean flag = false;
        for (int i = 0; i < cus_funi_list.get(idx).size(); i++)
            if (cus_funi_list.get(idx).get(i).equals(funi))
                flag = true;
        return flag;
    }

    public List<Integer> indexOfCusList(String name) {
        List<Integer> num = new ArrayList<Integer>();
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(0).equals(name))
                num.add(i);
        return num;
    }

    public int indexOfFuniList(String funi) {
        int num = 0;
        for (int i = 0; i < FUNITURES.size(); i++)
            if (FUNITURES.get(i).equals(funi))
                num = i;
        return num;
    }

    public int indexOfCusList_id(String id) {
        int num = 0;
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(1).equals(id))
                num = i;
        return num;
    }

    public boolean isInCusList(String name) {
        boolean flag = false;
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(0).equals(name))
                flag = true;
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
    public boolean isUsingID(String id){
        boolean flag = false;
        for (int i = 0; i < cus_funi_list.size(); i++)
            if (cus_funi_list.get(i).get(1).equals(id))
                flag = true;
        return flag;
    }
    public boolean add_cus(String name) {
        try{
            List<String> tmp = new ArrayList<String>();
            tmp.add(name);
            tmp.add(String.valueOf(nowID++));
            cus_funi_list.add(tmp);
            return true;
        }catch(Exception e){
            return false;
        }
    }
    public String add_cus_r(String name) {
        List<String> tmp = new ArrayList<String>();
        tmp.add(name);
        String id =String.valueOf(nowID++); 
        tmp.add(id);
        cus_funi_list.add(tmp);
        return id;
    }

    public boolean rental_funi(String id, String funi) {
        if (!isAvailableFuni(funi) || !isYouHaveStock(funi))
            return false;
        if (!calc_num_funis(funi, true))
            return false;
        cus_funi_list.get(indexOfCusList_id(id)).add(funi);
        return true;
    }

    public boolean return_funi(String id, String funi) {
        List<String> tmp = cus_funi_list.get(indexOfCusList_id(id));
        if (!isHavetargetfuni(tmp.get(1), funi))
            return false;
        if (!calc_num_funis(funi, false))
            return false;
        cus_funi_list.get(indexOfCusList_id(id)).remove(tmp.indexOf(funi));
        return true;
    }

    public boolean del_cus(String name) {
        if (!isInCusList(name))
            return false;
        int index = select_person(name);
        List<String> tmp = cus_funi_list.get(index);
        for (int i = 2; i < tmp.size(); i++)
            calc_num_funis(tmp.get(i), false);
        cus_funi_list.remove(index);
        return true;
    }

    public int count_funi(String id, String funi) {
        int count = 0;
        List<String> tmp = cus_funi_list.get(indexOfCusList_id(id));
        for (int i = 0; i < tmp.size(); i++)
            if (tmp.get(i).equals(funi))
                count++;
        return count;
    }

    public boolean entry_funi(String funi, int remain, int rented) {
        if (isAvailableFuni(funi)) {
            System.out.println("This is already in funis_list");
            return false;
        }
        List<Integer> tmp = new ArrayList<Integer>();
        FUNITURES.add(funi);
        tmp.add(remain);
        tmp.add(rented);
        funis_youhave.add(tmp);
        System.out.println("Complete entry " + funi);
        return true;
    }

    public boolean remove_funi(String funi) {
        if (!isAvailableFuni(funi)) {
            System.out.println(funi + " is not in Availabel list");
            return false;
        }
        int num = indexOfFuniList(funi);
        FUNITURES.remove(num);
        funis_youhave.remove(num);
        return true;

    }
    public boolean save_file(){
        try {
            FileWriter file;
            PrintWriter pw;
            
            file= new FileWriter("user_data.txt");
            pw = new PrintWriter(new BufferedWriter(file));
            for (int i=0;i<cus_funi_list.size();i++){
                List<String> tmp = cus_funi_list.get(i);
                if (i==0)
                    pw.println(String.valueOf(nowID));
                else{
                    for (int j=0;j<tmp.size();j++){
                        pw.print(tmp.get(j));
                        if (j!=tmp.size()-1)
                            pw.print(",");
                    }
                    if (i!=cus_funi_list.size()-1)
                        pw.print("\n");
                }
            }
            pw.close();

            file= new FileWriter("funis_data.txt");
            pw = new PrintWriter(new BufferedWriter(file));
            for (int i=0;i<funis_youhave.size();i++){
                List<Integer> tmp = funis_youhave.get(i);
                pw.print(FUNITURES.get(i)+","+tmp.get(0)+","+tmp.get(1));
                if (i!=funis_youhave.size()-1)
                    pw.print("\n");
            }
            pw.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }
    public static void main(String[] args) {

        funi_second a = new funi_second();
        for (;;) {
            Scanner scan = new Scanner(System.in);
            System.out.println("Enter admin/customer/new end to \"close\"");
            String str = scan.nextLine();
            switch (str) {
                case "admin":
                    for (;;) {
                        System.out.println("");
                        System.out.println("Enter Your Order: ");
                        System.out.println("ADD New Customer : ac");
                        System.out.println("Rent Furniture : af");

                        System.out.println("Delete Customer : dc");
                        System.out.println("Return Furniture : df");

                        System.out.println("Show Num Of Funitures (remaining/rented): sf");
                        System.out.println("Show ALL Customers Information: sc");

                        System.out.println("Entry funitures customer can rent : ef");
                        System.out.println("Remove funitures customer can rent : rf");

                        System.out.println("Return : return");
                        System.out.println("Close : close");
                        System.out.println("");

                        String order = scan.nextLine();
                        if (order.equals("return"))
                            break;
                        String name, funi, idx;
                        String[] names, funis;
                        boolean r=true;
                        switch (order) {
                            case "ac":
                                // ADD Customer
                                System.out.println(
                                        "Enter New Customers you need to add (Plz split with ,)");
                                names = scan.nextLine().split(",");
                                for (int i = 0; i < names.length; i++)
                                    r = a.add_cus(names[i]);
                                    if (r)
                                        System.out.println("Complete add");
                                    else
                                        System.out.println("Miss to add");
                                break;
                            case "af":
                                // ADD Funiture
                                System.out.println("Enter Target Customer you need to add");
                                name = scan.nextLine();
                                if (!a.isInCusList(name)){
                                    System.out.println("Target is not member");break;
                                }
                                idx = String.valueOf(a.select_person(name));
                                System.out.println("Enter Funitures you need rent (Plz split with ,)");
                                funis = scan.nextLine().split(",");
                                for (int i = 0; i < funis.length; i++){
                                    r = a.rental_funi(idx, funis[i]);
                                    if (r)
                                        System.out.println("Complete add");
                                    else
                                        System.out.println("Miss to add");
                                }
                                break;
                            case "dc":
                                // DELETE Customers
                                System.out.println(
                                        "Enter Names you need to DELETE (Plz split with ,)");
                                names = scan.nextLine().split(",");
                                for (int i = 0; i < names.length; i++)
                                    r = a.del_cus(names[i]);
                                    if (r)
                                        System.out.println("Complete delete customer");
                                    else
                                        System.out.println("Miss to delete");
                                break;
                            case "df":
                                // DELETE Funitures
                                System.out.println("Enter Target Customer you need to DELETE");
                                name = scan.nextLine();
                                if (!a.isInCusList(name)){
                                    System.out.println(name + " is not member");
                                    break;
                                }
                                int index = a.select_person(name);
                                System.out.println("Enter Funitures you need DELETE (Plz split with ,)");
                                funis = scan.nextLine().split(",");
                                String id = cus_funi_list.get(index).get(1);
                                for (int i=0; i < funis.length; i++)
                                    r = a.return_funi(id, funis[i]);
                                    if (r)
                                        System.out.println("Complete delete");
                                    else
                                        System.out.println("Miss to delete");
                                break;
                            case "sf":
                                a.print_sf();
                                break;
                            case "sc":
                                a.print_sc();
                                break;
                            case "ef":
                                System.out.println("Enter One funiture you ADD to funis_list");
                                funi = scan.nextLine();
                                System.out.println("Enter Nums now remaining");
                                String num1 = scan.nextLine();
                                System.out.println("Enter Nums now rented");
                                String num2 = scan.nextLine();
                                r = a.entry_funi(funi, Integer.valueOf(num1), Integer.valueOf(num2));
                                if (r)
                                    System.out.println("Complete entry");
                                else
                                    System.out.println("Miss to entry");
                                break;
                            case "rf":
                                System.out.println("Enter Funis you REMOVE funis_list (pls split with ,)");
                                funis = scan.nextLine().split(",");
                                for (int i = 0; i < funis.length; i++)
                                    r = a.remove_funi(funis[i]);
                                    if (r)
                                        System.out.println("Complete remove");
                                    else
                                        System.out.println("Miss to remove");

                                break;
                            case "close":
                                boolean q = a.save_file();
                                if (q)
                                    System.out.println("Complete save");
                                else
                                    System.out.println("Miss to save");
                                System.out.println("See you!!");
                                System.exit(1);
                            default:
                                System.out.println(order + ", This Order is not AVAILABLE");
                                break;
                        }
                        System.out.println(cus_funi_list);
                        System.out.println(FUNITURES);
                        System.out.println(funis_youhave);
                        System.out.println(nowID);
                    }
                    break;
                case "customer":
                    String id;
                    for (;;){
                        System.out.println("Pls Enter Your ID");
                        id = scan.nextLine();
                        if (!a.isUsingID(id)){
                            System.out.println("The ID is not exist");
                            continue;
                        }
                        break;
                    }
                    for (;;){
                        
                        System.out.println("");
                        System.out.println("Enter Your Order: ");
                        System.out.println("Rent Furniture : af");
                        System.out.println("Return Furniture : df");
                        System.out.println("Delete Your ID : dc");
                        System.out.println("Show Your Rental Info : sc");
                        System.out.println("Return : return");
                        System.out.println("Close : close");
                        System.out.println("");

                        String order = scan.nextLine();
                        if (order.equals("return"))
                            break;
                        
                        boolean r =true;
                        switch (order){
                            case "af":
                                System.out.println("choose funis you want to RENTAL");
                                for (int i=0;i<FUNITURES.size();i++){
                                    System.out.println(FUNITURES.get(i));
                                }
                                str = scan.nextLine();
                                r = a.rental_funi(id, str);

                                if (r)
                                    System.out.println("Complete to RENT");
                                else
                                    System.out.println("Miss to RENT");
                                break;
                            case "df":
                                System.out.println("choose funis you want to RETURN");
                                a.print_by_id(id);
                                str = scan.nextLine();
                                r = a.return_funi(id, str);
                                if (r)
                                    System.out.println("Complete to RETURN");
                                else
                                    System.out.println("Miss to RETURN");
                                break;
                            case "sc":
                                a.print_by_id(id);
                                break;
                            case "close":
                                boolean q = a.save_file();
                                if (q)
                                    System.out.println("Complete save");
                                else
                                    System.out.println("Miss to save");
                                System.out.println("See you!!");
                                System.exit(1);
                            default:
                                System.out.println(order + ", This Order is not AVAILABLE");
                                break;
                        }
                    }
                    break;
                    
                case "new":
                    // ADD Customer
                    System.out.println(
                            "Enter your name");
                    String name = scan.nextLine();
                    String newid = a.add_cus_r(name);
                    System.out.println("Complete add");
                    System.out.println("Your ID is "+newid);
                    System.out.println("Enjoy Rental Funitures");
                    break;
                case "close":
                    boolean q = a.save_file();
                    if (q)
                        System.out.println("Complete save");
                    else
                        System.out.println("Miss to save");
                    System.out.println("See you!!");
                    System.exit(1);
                default:
                    System.out.println("pls select in admin/customer/new");
                    break;
            }
        }
    }
}
