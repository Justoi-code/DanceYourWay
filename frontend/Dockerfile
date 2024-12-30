# Use Node.js base image
FROM node:16

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the code
COPY . .

# Expose Expo development ports
EXPOSE 19000 19001

# Command to start the Expo server
CMD ["npm", "start"]
