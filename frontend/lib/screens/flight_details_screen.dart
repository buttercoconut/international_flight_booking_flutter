import 'package:flutter/material.dart';
import 'package:international_flight_booking/models/flight.dart';
import 'package:international_flight_booking/screens/booking_confirmation_screen.dart';

class FlightDetailsScreen extends StatelessWidget {
  static const routeName = '/details';

  const FlightDetailsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final flight = ModalRoute.of(context)!.settings.arguments as Flight;

    return Scaffold(
      appBar: AppBar(title: Text('Flight ${flight.flightNumber} Details')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Origin: ${flight.origin}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 8),
            Text('Destination: ${flight.destination}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 8),
            Text('Departure: ${flight.departureTime}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 8),
            Text('Arrival: ${flight.arrivalTime}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 8),
            Text('Status: ${flight.status}', style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(
                  context,
                  BookingConfirmationScreen.routeName,
                );
              },
              child: const Text('Book Flight'),
            ),
          ],
        ),
      ),
    );
  }
}
