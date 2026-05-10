import 'package:flutter/material.dart';
import 'package:international_flight_booking_flutter/screens/flight_search_screen.dart';

void main() {
  runApp(const InternationalFlightBookingApp());
}

class InternationalFlightBookingApp extends StatelessWidget {
  const InternationalFlightBookingApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'International Flight Booking',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const FlightSearchScreen(),
    );
  }
}