package com.example.finalproject;

public class ImageItem {
    private String imageUrl;
    private String title;

    public ImageItem(String imageUrl, String title) {
        this.imageUrl = imageUrl;
        this.title = title;
    }

    public String getImageUrl() { return imageUrl; }
    public String getTitle() { return title; }
}

