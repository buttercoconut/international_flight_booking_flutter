import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import '../screens/home_screen.dart';
import '../screens/search_screen.dart';
import '../screens/booking_screen.dart';

void main() {
  runApp(InternationalFlightBookingApp());
}

class InternationalFlightBookingApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'International Flight Booking',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => HomeScreen(),
        '/search': (context) => SearchScreen(),
        '/booking': (context) => BookingScreen(),
      },
    );
  }
}
