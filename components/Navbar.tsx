import React from 'react'
import Link from 'next/link'

export default function Navbar(){
  return (
    <header style={{
      background: 'linear-gradient(135deg, rgba(10, 61, 98, 0.02) 0%, rgba(0, 61, 153, 0.01) 100%)',
      boxShadow: '0 1px 3px rgba(10, 61, 98, 0.1)'
    }} className="border-b">
      <div style={{maxWidth: '1280px', margin: '0 auto', padding: '1.5rem 1.5rem'}} className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 rounded-lg flex items-center justify-center font-bold text-white" style={{backgroundColor: 'var(--accent)'}}>
            D
          </div>
          <div>
            <Link href="/" className="text-lg font-semibold transition-all duration-200 block" style={{fontFamily: 'Roboto Mono, ui-monospace, SFMono-Regular', color: 'var(--primary)'}}>
              Data Science Club
            </Link>
            <div className="text-xs text-slate-600" style={{color: 'var(--accent)'}}>Leading the way with difference</div>
          </div>
        </div>

        <nav>
          <ul className="flex space-x-8 text-sm">
            <li><Link href="/" className="font-medium transition-all duration-200 hover:text-blue-800 relative group" style={{color: 'var(--primary)'}}>
              Home
              <span className="absolute bottom-0 left-0 w-0 h-0.5 group-hover:w-full" style={{backgroundColor: 'var(--accent)', transition: 'width 0.3s ease'}}></span>
            </Link></li>
            <li><Link href="/about" className="font-medium transition-all duration-200 hover:text-blue-800 relative group" style={{color: 'var(--primary)'}}>
              About Us
              <span className="absolute bottom-0 left-0 w-0 h-0.5 group-hover:w-full" style={{backgroundColor: 'var(--accent)', transition: 'width 0.3s ease'}}></span>
            </Link></li>
            <li><Link href="/initiatives" className="font-medium transition-all duration-200 hover:text-blue-800 relative group" style={{color: 'var(--primary)'}}>
              Initiatives
              <span className="absolute bottom-0 left-0 w-0 h-0.5 group-hover:w-full" style={{backgroundColor: 'var(--accent)', transition: 'width 0.3s ease'}}></span>
            </Link></li>
            <li><Link href="/team" className="font-medium transition-all duration-200 hover:text-blue-800 relative group" style={{color: 'var(--primary)'}}>
              Team
              <span className="absolute bottom-0 left-0 w-0 h-0.5 group-hover:w-full" style={{backgroundColor: 'var(--accent)', transition: 'width 0.3s ease'}}></span>
            </Link></li>
          </ul>
        </nav>
      </div>
    </header>
  )
}
