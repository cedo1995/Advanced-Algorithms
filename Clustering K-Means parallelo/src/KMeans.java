import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class KMeans{
    void serialKMeans(List<City> cities, int k, int num_it){
        int n = cities.size();

        cities.sort((a,b )-> a.getPopulation() - b.getPopulation());
        Collections.reverse(cities);

        List<City> firstFifty = cities.subList(0,50);

        List<Point> centroids = new ArrayList<Point>();

        for (City a:firstFifty){
            centroids.add(new Point(a.latitude, a.longitude));
            //System.out.println(a);
        }
        
    }

}