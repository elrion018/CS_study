import java.io.*;
import java.util.*;

public class no14503 {
  static int stoi(String s) {
    return Integer.parseInt(s);
  }

  static int[] dr = { -1, 0, 1, 0 };
  static int[] dc = { 0, 1, 0, -1 };
  static int[][] map;
  static int r, c, d;
  static int N;
  static int M;
  // static int turnCount = 0;

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());

    N = stoi(st.nextToken());
    M = stoi(st.nextToken());
    map = new int[N][M];

    st = new StringTokenizer(br.readLine());
    r = stoi(st.nextToken());
    c = stoi(st.nextToken());
    d = stoi(st.nextToken());

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        map[i][j] = stoi(st.nextToken());
      }

    }

    run(r, c, d, 0);

  }

  static void run(int r, int c, int d, int turnCount) {
    clean(r, c, d, turnCount);
    return;
  }

  static void cal() {
    int result = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (map[i][j] == 2) {
          result += 1;
        }
      }

    }
    System.out.println(result);
    return;
  }

  static void search(int r, int c, int d, int turnCount) {

    int ad = rotate(d);
    int ar = r + dr[ad];
    int ac = c + dc[ad];
    int ar2 = r - dr[d];
    int ac2 = c - dc[d];

    if (turnCount == 4 && map[ar2][ac2] == 1) {
      cal();
      return;
    }

    if (turnCount == 4) {
      search(ar2, ac2, d, 0);
      return;
    }

    if (map[ar][ac] == 0) {
      clean(ar, ac, ad, 0);
      return;

    }

    if (map[ar][ac] == 1 || map[ar][ac] == 2) {
      search(r, c, ad, turnCount + 1);
      return;
    }

  }

  static void clean(int r, int c, int d, int turnCount) {
    map[r][c] = 2;
    search(r, c, d, turnCount);
    return;
  }

  static int rotate(int d) {
    if (d == 0) {
      return 3;
    }

    d = d - 1;
    return d;
  }
}