public class City {
    int id;
    String name;
    int population;
    double latitude;
    double longitude;

    public City(String[] values) {
        this.id = Integer.parseInt(values[0]);
        this.name = values[1];
        this.population = Integer.parseInt(values[2]);;
        this.latitude = Double.parseDouble(values[3]);;
        this.longitude = Double.parseDouble(values[4]);;
    }

    @Override
    public String toString() {
        return "[" + this.id + ", " + this.name + ", " + this.population + ", " + this.latitude + ", " + this.longitude +"]";
    }
}
