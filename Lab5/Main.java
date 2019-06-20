import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    private static final String SAMPLE_CSV_FILE_PATH = "./src/cities-and-towns-of-usa.csv";

    public static void main(String[] args) {
        List<City> citiesList = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(SAMPLE_CSV_FILE_PATH))) {
            String line;
            br.readLine();
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                City city = new City(values);
                System.out.println(city);
                citiesList.add(city);
            }
        }
        catch(Exception e) {
            System.out.println(e);
        }

    }
}
