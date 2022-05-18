import React from "react";
import { Link } from "react-router-dom";
import styles from "./RegisterForm.module.css";

const RegisterForm = () => {
  return (
    <div className={styles.center}>
      <h1>Register</h1>
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
        <input type="submit" value="Register" />
      </form>
      <div className={styles.redirect}>
        <Link to="/" style={{ color: "black" }}>
          Go Home
        </Link>
      </div>
    </div>
  );
};

export default RegisterForm;
