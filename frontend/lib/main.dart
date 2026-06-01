import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'models/flight.dart';
import 'services/api_service.dart';
import 'screens/flight_search_screen.dart';
import 'screens/flight_comparison_screen.dart';
import 'screens/booking_screen.dart';
import 'screens/booking_confirmation_screen.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => FlightProvider()),
      ],
      child: const InternationalFlightBookingApp(),
    ),
  );
}

class InternationalFlightBookingApp extends StatelessWidget {
  const InternationalFlightBookingApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'International Flight Booking',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      initialRoute: '/search',
      routes: {
        '/search': (_) => const FlightSearchScreen(),
        '/compare': (_) => const FlightComparisonScreen(),
        '/booking': (_) => const BookingScreen(),
        '/confirmation': (_) => const BookingConfirmationScreen(),
      },
    );
  }
}

class FlightProvider extends ChangeNotifier {
  List<Flight> _flights = [];
  List<Flight> get flights => _flights;

  void setFlights(List<Flight> flights) {
    _flights = flights;
    notifyListeners();
  }
}
