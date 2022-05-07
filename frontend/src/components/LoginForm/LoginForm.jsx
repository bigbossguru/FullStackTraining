import React from "react";
import { Link } from "react-router-dom";
import styles from "./LoginForm.module.css";

const LoginForm = () => {
  return (
    <div className={styles.center}>
      <h1>Login</h1>
      <form method="post">
        <div className={styles.field}>
          <input type="text" required />
          <span></span>
          <label>Email</label>
        </div>
        <div className={styles.field}>
          <input type="password" required />
          <span></span>
          <label>Password</label>
        </div>
        <input type="submit" value="Login" />
      </form>
      <div className={styles.redirect}>
        <Link to="/" style={{ color: "black" }}>
          Go Home
        </Link>
      </div>
    </div>
  );
};

export default LoginForm;
