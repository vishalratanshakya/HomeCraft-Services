const mongoose = require('mongoose');
const Admin = require('./models/Admin');
require('dotenv').config();

mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(async () => {
    const admins = await Admin.find({});
    console.log("Admins:", admins.map(a => a.email));
    
    if (admins.length === 0) {
      const newAdmin = new Admin({
        name: 'Super Admin',
        email: 'admin@homecraft.com',
        password: 'password123',
        role: 'superadmin',
        isActive: true
      });
      await newAdmin.save();
      console.log('Created admin@homecraft.com / password123');
    } else {
      const a = admins[0];
      a.password = 'password123';
      a.email = 'admin@homecraft.com';
      await a.save();
      console.log('Reset password for admin@homecraft.com to password123');
    }
    process.exit(0);
  });
