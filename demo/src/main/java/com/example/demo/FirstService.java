package com.example.demo;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
public class FirstService {

    Bilgi bilgi= new Bilgi();



    @RequestMapping("/string")
    @ResponseBody
    String home(String result) {
        return bilgi.getResult();
    }


    public FirstService() throws IOException {
    }


}