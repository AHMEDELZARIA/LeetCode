class TransposeMatrix {
    public int[][] transpose(int[][] matrix) {
        int [][] op = new int[matrix[0].length][matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                op[j][i] = matrix[i][j];
            }
        }
        return op;
    }
}
