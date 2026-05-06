import React, { ReactNode } from 'react'
import Navbar from './Navbar'
import Footer from './Footer'

type Props = { children: ReactNode }

export default function Layout({ children }: Props){
  return (
    <div className="min-h-screen flex flex-col bg-white text-slate-950">
      <Navbar />
      <main className="flex-1 mx-auto w-full" style={{maxWidth: '1280px', padding: '3rem 1.5rem'}}>
        {children}
      </main>
      <Footer />
    </div>
  )
}
