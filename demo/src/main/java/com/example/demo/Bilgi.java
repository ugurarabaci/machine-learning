package com.example.demo;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.IOException;

public class Bilgi {

    String page = "https://www.tutorialspoint.com/";
    //Connecting to the web page
    Connection conn = Jsoup.connect(page);
    //executing the get request
    Document doc = conn.get();
    //Retrieving the contents (body) of the web page
    String result = doc.body().text();

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }
    public Bilgi() throws IOException {
    }
}
