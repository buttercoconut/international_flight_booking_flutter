class Flight {
  final String flightNumber;
  final String airline;
  final String origin;
  final String destination;
  final DateTime departureTime;
  final DateTime arrivalTime;
  final double price;
  final bool isDirect;

  Flight({
    required this.flightNumber,
    required this.airline,
    required this.origin,
    required this.destination,
    required this.departureTime,
    required this.arrivalTime,
    required this.price,
    required this.isDirect,
  });

  factory Flight.fromJson(Map<String, dynamic> json) {
    return Flight(
      flightNumber: json['flightNumber'] as String,
      airline: json['airline'] as String,
      origin: json['origin'] as String,
      destination: json['destination'] as String,
      departureTime: DateTime.parse(json['departureTime'] as String),
      arrivalTime: DateTime.parse(json['arrivalTime'] as String),
      price: (json['price'] as num).toDouble(),
      isDirect: json['isDirect'] as bool,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'flightNumber': flightNumber,
      'airline': airline,
      'origin': origin,
      'destination': destination,
      'departureTime': departureTime.toIso8601String(),
      'arrivalTime': arrivalTime.toIso8601String(),
      'price': price,
      'isDirect': isDirect,
    };
  }
}
