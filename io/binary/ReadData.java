import java.io.*;

class ReadData {
	public static void main(String[] args) {
		try (DataInputStream is = 
				new DataInputStream(new FileInputStream("/tmp/x.y"))) {
			int i = is.readInt();
			System.out.println(i);
			int j = is.read();
			System.out.println(j);
		} catch (IOException e) {
			System.out.println(e.toString());
		}
	}
}
