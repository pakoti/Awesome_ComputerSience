% Sample data for a candlestick chart
% Replace this with your own data
openPrices = [100, 110, 115, 105, 120];
closePrices = [105, 112, 118, 107, 119];
highPrices = [115, 120, 125, 115, 125];
lowPrices = [95, 105, 110, 100, 110];
dates = 1:5; % x-axis representing time

% Create a figure
figure;

% Plot candlesticks
candle(highPrices, lowPrices, openPrices, closePrices, 'r', 'g', 'w', dates);

% Add labels and title
xlabel('Time Period');
ylabel('Price');
title('Candlestick Chart');

% Customize the x-axis labels
xticks(dates);
xticklabels({'Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'});

% Add grid lines
grid on;

% Display the chart
