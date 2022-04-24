import mongoose from "mongoose";

mongoose.connect("mongodb+srv://joaont:122012@node.qaahn.mongodb.net/node-livros?");

let db = mongoose.connection;

export default db;