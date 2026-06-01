import 'package:flutter/material.dart';
import 'package:international_flight_booking/models/flight.dart';
import 'package:international_flight_booking/services/flight_service.dart';
import 'package:international_flight_booking/widgets/flight_card.dart';

class FlightSearchScreen extends StatefulWidget {
  static const routeName = '/search';

  const FlightSearchScreen({Key? key}) : super(key: key);

  @override
  _FlightSearchScreenState createState() => _FlightSearchScreenState();
}

class _FlightSearchScreenState extends State<FlightSearchScreen> {
  final FlightService _flightService = FlightService();
  List<Flight> _flights = [];
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _searchFlights();
  }

  Future<void> _searchFlights() async {
    setState(() => _isLoading = true);
    try {
      final flights = await _flightService.searchFlights(
        origin: 'NYC',
        destination: 'LHR',
        date: DateTime.now(),
        passengers: 1,
      );
      setState(() => _flights = flights);
    } catch (e) {
      // Handle error
    } finally {
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Search Flights')),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: _flights.length,
              itemBuilder: (context, index) {
                final flight = _flights[index];
                return FlightCard(
                  flight: flight,
                  onTap: () {
                    Navigator.pushNamed(
                      context,
                      FlightDetailsScreen.routeName,
                      arguments: flight,
                    );
                  },
                );
              },
            ),
    );
  }
}
