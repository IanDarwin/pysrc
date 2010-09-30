import java.io.*;

class ReadData {
	public static void main(String[] args) {
		DataInputStream is = null;
		try {
			is = new DataInputStream(new FileInputStream("/tmp/x.y"));
			int i = is.readInt();
			System.out.println(i);
			int j = is.read();
			System.out.println(j);
		} catch (IOException e) {
			System.out.println(e.toString());
		} finally {
			try {
				is.close();
			} catch (IOException e) {
				// empty
			}
		}
	}
}
