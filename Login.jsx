import React from 'react'
import '../Pages/CSS/Login.css'

const Login = () => {

  return (
    <section className="loginsignup">
      <div className="form-box">
        <div className="loginsignup-container">
          <h2>Login</h2>
          <div className="loginsignup-fields">
            <div className="inputbox">
              <input name='email' type="text" required />
              <label>Email</label>
            </div>
            <div className="inputbox">
              <input name='password' type="password" required />
              <label>Password</label>
            </div>
          </div>
          <button className='login-button'>Continue</button>
          <div className="forget">
            <label>
              <input type="checkbox" /> By continuing, I agree to the <span className="terms-link">terms of use</span> & <span className="privacy-link">privacy policy</span>.
            </label>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Login