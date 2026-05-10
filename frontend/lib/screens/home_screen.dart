import 'package:flutter/material.dart';
import '../widgets/flight_card.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('International Flight Booking')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.pushNamed(context, '/search');
          },
          child: Text('Search Flights'),
        ),
      ),
    );
  }
}
