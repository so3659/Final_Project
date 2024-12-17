package com.example.finalproject;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.net.URL;
import java.util.List;

public class CustomAdapter extends ArrayAdapter<ImageItem> {
    private Context context;
    private List<ImageItem> items;

    public CustomAdapter(Context context, List<ImageItem> items) {
        super(context, R.layout.list_item, items);
        this.context = context;
        this.items = items;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.list_item, parent, false);
        }

        ImageView imageView = convertView.findViewById(R.id.imageView);
        TextView textView = convertView.findViewById(R.id.textView);

        ImageItem item = items.get(position);
        textView.setText(item.getTitle());

        // 이미지 로딩은 별도의 스레드에서 수행
        new Thread(() -> {
            try {
                URL url = new URL(item.getImageUrl());
                final Bitmap bitmap = BitmapFactory.decodeStream(url.openStream());
                imageView.post(() -> imageView.setImageBitmap(bitmap));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }).start();

        return convertView;
    }
}
