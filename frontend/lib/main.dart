import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'screens/flight_search_screen.dart';
import 'screens/flight_comparison_screen.dart';
import 'screens/booking_screen.dart';
import 'screens/booking_confirmation_screen.dart';
import 'services/api_service.dart';

void main() {
  runApp(const InternationalFlightBookingApp());
}

class InternationalFlightBookingApp extends StatelessWidget {
  const InternationalFlightBookingApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider(create: (_) => ApiService()),
      ],
      child: MaterialApp(
        title: 'International Flight Booking',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        initialRoute: '/',
        routes: {
          '/': (_) => const FlightSearchScreen(),
          '/compare': (_) => const FlightComparisonScreen(),
          '/booking': (_) => const BookingScreen(),
          '/confirmation': (_) => const BookingConfirmationScreen(),
        },
      ),
    );
  }
}
