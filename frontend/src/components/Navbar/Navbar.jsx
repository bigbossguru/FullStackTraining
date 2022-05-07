import React from "react";
import styles from "./Navbar.module.css";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <header>
      <a href="#home" className={styles.logo}>
        <h2>FullStackTrainig</h2>
      </a>
      <nav>
        <ul className={styles.nav_links}>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/form">Form</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>
      <Link to="/login">
        <button>Login</button>
      </Link>
    </header>
  );
};

export default Navbar;
