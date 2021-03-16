package com.example.demo;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) throws IOException {
		FirstService fs = new FirstService();
		SpringApplication.run(DemoApplication.class, args);
		//Bilgi bilgi = new Bilgi();
		//String a= bilgi.getBaslik();
		//FirstService fs = new FirstService();
		//String ilanNo = "912981961";
		//fs.bilgiScrap(ilanNo);
		//System.out.println(bilgi.getBaslik());

	}

}
