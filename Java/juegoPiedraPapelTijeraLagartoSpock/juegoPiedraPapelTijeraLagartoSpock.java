package Java.juegoPiedraPapelTijeraLagartoSpock;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

public class juegoPiedraPapelTijeraLagartoSpock {

    // Definir constantes para las jugadas
    private static final String SCISSORS = "scissors";
    private static final String PAPER = "paper";
    private static final String ROCK = "rock";
    private static final String LIZARD = "lizard";
    private static final String SPOCK = "spock";

    public static void main(String[] args) {
        // Definir las jugadas
        String player1 = ROCK;
        String player2 = PAPER;

        // Llamar al método rpsls
        System.out.println(rpsls(player1, player2));
    }

    // Definir el método rpsls
    public static String rpsls(String player1, String player2) {
        // Crear el HashMap con List como valor
        HashMap<String, List<String>> gameRules = new HashMap<>();

        // Agregar las claves y una lista de valores
        gameRules.put(SCISSORS, new ArrayList<>(List.of(PAPER, LIZARD)));
        gameRules.put(PAPER, new ArrayList<>(List.of(ROCK, SPOCK)));
        gameRules.put(ROCK, new ArrayList<>(List.of(LIZARD, SCISSORS)));
        gameRules.put(LIZARD, new ArrayList<>(List.of(SPOCK, PAPER)));
        gameRules.put(SPOCK, new ArrayList<>(List.of(SCISSORS, ROCK)));

        // Validar las entradas
        if (!gameRules.containsKey(player1) || !gameRules.containsKey(player2)) {
            return "Invalid input! Please choose scissors, paper, rock, lizard, or spock.";
        }

        // Verificar si player1 gana
        if (gameRules.get(player1).contains(player2)) {
            return "Player 1 Won!";
        }
        // Verificar si player2 gana
        else if (gameRules.get(player2).contains(player1)) {
            return "Player 2 Won!";
        }

        // Si no gana ninguno, es empate
        return "Draw!";
    }
}
