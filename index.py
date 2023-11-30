public class SatisfacaoCliente {

    public static void main(String[] args) {
    
        int posicaoCliente = 3; 
        int tempoEntrega = 45; 
        int satisfacao = getSatisfacao(posicaoCliente, tempoEntrega);
        System.out.println("Satisfação do cliente: " + satisfacao);
    
    }

    public static int getSatisfacao(int posicaoCliente, int tempoEntrega) {
        
        int satisfacao = 0;

        if (posicaoCliente <= 5 && tempoEntrega <= 30) {
            satisfacao = 5; // Máxima satisfação
        } else if (posicaoCliente <= 10 && tempoEntrega <= 60) {
            satisfacao = 3; // Satisfação moderada
        } else {
            satisfacao = 1; // Baixa satisfação
        }

        return satisfacao;
    }
}
