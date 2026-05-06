import React from 'react'
import Link from 'next/link'

export default function Footer(){
  return (
    <footer style={{background: 'linear-gradient(135deg, #f0f7ff 0%, rgba(0, 61, 153, 0.03) 100%)'}}>
      {/* Main Footer */}
      <div style={{maxWidth: '1280px', margin: '0 auto', padding: '3rem 1.5rem'}}>
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          {/* About */}
          <div>
            <div className="flex items-center mb-3">
              <div className="w-8 h-8 rounded-lg flex items-center justify-center font-bold text-white text-sm mr-2" style={{backgroundColor: 'var(--accent)'}}>
                D
              </div>
              <div className="font-semibold text-lg" style={{color: 'var(--primary)'}}>Data Science Club</div>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed mb-4">A professional community advancing data literacy and rigorous scholarship through education, research, and collaborative impact.</p>
            <div className="mt-4 flex space-x-4">
              <a href="#" className="w-8 h-8 rounded-lg flex items-center justify-center text-white text-sm transition-all duration-300 hover:scale-110" style={{backgroundColor: 'var(--accent)', opacity: 0.8}} title="Facebook">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                </svg>
              </a>
              <a href="#" className="w-8 h-8 rounded-lg flex items-center justify-center text-white text-sm transition-all duration-300 hover:scale-110" style={{backgroundColor: 'var(--accent)', opacity: 0.8}} title="Instagram">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0m0 2c5.514 0 10 4.486 10 10s-4.486 10-10 10S2 17.514 2 12 6.486 2 12 2m3 5.5a1.5 1.5 0 110-3 1.5 1.5 0 010 3m-6 0a4 4 0 110-8 4 4 0 010 8m0-2a2 2 0 100-4 2 2 0 000 4"/>
                </svg>
              </a>
              <a href="#" className="w-8 h-8 rounded-lg flex items-center justify-center text-white text-sm transition-all duration-300 hover:scale-110" style={{backgroundColor: 'var(--accent)', opacity: 0.8}} title="LinkedIn">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.475-2.236-1.986-2.236-1.081 0-1.722.722-2.004 1.418-.103.249-.129.597-.129.946v5.441h-3.554s.05-8.836 0-9.759h3.554v1.383c.43-.664 1.199-1.61 2.919-1.61 2.134 0 3.734 1.39 3.734 4.38v5.606zM5.337 8.855c-1.144 0-1.915-.758-1.915-1.71 0-.956.768-1.71 1.959-1.71 1.19 0 1.916.754 1.935 1.71 0 .952-.745 1.71-1.979 1.71zm1.582 11.597H3.714v-9.759h3.205v9.759zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
              </a>
            </div>
          </div>

          {/* Explore */}
          <div>
            <div className="font-semibold mb-4 flex items-center" style={{color: 'var(--primary)'}}>
              <span className="inline-block w-1.5 h-1.5 rounded-full mr-2" style={{backgroundColor: 'var(--accent)'}}></span>
              Explore
            </div>
            <ul className="text-sm space-y-2 text-slate-700">
              <li><Link href="/" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>Home</Link></li>
              <li><Link href="/about" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>About Us</Link></li>
              <li><Link href="/initiatives" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>Initiatives</Link></li>
              <li><Link href="/team" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>Team</Link></li>
            </ul>
          </div>

          {/* Resources */}
          <div>
            <div className="font-semibold mb-4 flex items-center" style={{color: 'var(--primary)'}}>
              <span className="inline-block w-1.5 h-1.5 rounded-full mr-2" style={{backgroundColor: 'var(--accent)'}}></span>
              Resources
            </div>
            <ul className="text-sm space-y-2 text-slate-700">
              <li><a href="#" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>Class Schedule</a></li>
              <li><a href="#" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>Membership</a></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <div className="font-semibold mb-4 flex items-center" style={{color: 'var(--primary)'}}>
              <span className="inline-block w-1.5 h-1.5 rounded-full mr-2" style={{backgroundColor: 'var(--accent)'}}></span>
              Contact
            </div>
            <p className="text-sm text-slate-700 mb-3">Reach out to us</p>
            <div className="text-sm text-slate-700 space-y-1">
              <div><a href="tel:+1234567890" className="hover:font-medium transition-all duration-300" style={{color: 'var(--primary)'}}>+1 (234) 567-890</a></div>
              <div><a href="mailto:info@datascienceclub.edu" className="hover:font-medium transition-all duration-300 break-all" style={{color: 'var(--primary)'}}>info@datascienceclub.edu</a></div>
            </div>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-blue-200 my-8" style={{borderColor: 'rgba(0, 61, 153, 0.2)'}}></div>

        {/* Bottom Footer */}
        <div className="text-center text-xs text-slate-600 space-y-2">
          <div>
            © 2025 Data Science Club. All rights reserved | <a href="#" className="hover:underline" style={{color: 'var(--primary)'}}>Privacy Policy</a> | <a href="#" className="hover:underline" style={{color: 'var(--primary)'}}>Terms of Service</a>
          </div>
          <div style={{color: 'rgba(0, 61, 153, 0.6)'}}>
            Designed with care for academic excellence and community impact
          </div>
        </div>
      </div>
    </footer>
  )
}
