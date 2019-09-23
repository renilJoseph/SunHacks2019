package models;

import java.util.Objects;

public class Obstacle {
    private String type;
    private String position;

    public Obstacle() {}

    public Obstacle(String type, String position) {
        this.type = type;
        this.position = position;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Obstacle obstacle = (Obstacle) o;
        return Objects.equals(type, obstacle.type) &&
                Objects.equals(position, obstacle.position);
    }

    @Override
    public int hashCode() {
        return Objects.hash(type, position);
    }

    @Override
    public String toString() {
        return "Obstacle{" +
                "type='" + type + '\'' +
                ", position='" + position + '\'' +
                '}';
    }
}
