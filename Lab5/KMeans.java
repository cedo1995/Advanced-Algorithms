import Comparator;
import java.util.Arrays;
import java.util.List;


public static class KMeans{
    public List<List<City>> serialKMeans(List<City> cities, int k, int num_it){
        int n = len(cities);
        cities.sort(new Comparator<City>(){
            public int compare(City a, City b){
                return b.getPopulation() - a.getPopulation();
            }
        });
        for (City a:cities){
            System.out.println(a);
        }
    }

}