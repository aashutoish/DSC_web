import React from 'react'
import Head from 'next/head'
import { useRouter } from 'next/router'
import Link from 'next/link'
import programs from '../../data/initiatives'

export default function InitiativeDetail(){
  const router = useRouter()
  const { slug } = router.query

  const program = programs.find(p => p.slug === slug)

  if (!program) {
    return (
      <div className="py-12">
        <Head><title>Initiative — Not found</title></Head>
        <h2 className="text-2xl font-semibold" style={{color: 'var(--primary)'}}>Initiative not found</h2>
        <p className="mt-4 text-slate-700">We couldn't find that initiative. Browse our list of initiatives below.</p>
        <div className="mt-6"><Link href="/initiatives" className="text-sm font-medium" style={{color: 'var(--accent)'}}>Back to Initiatives</Link></div>
      </div>
    )
  }

  return (
    <div className="py-12">
      <Head><title>{program.title} — Data Science Club</title></Head>

      <div className="mb-6">
        <Link href="/initiatives" className="text-sm font-medium" style={{color: 'var(--accent)'}}>← Back to Initiatives</Link>
      </div>

      <h1 className="text-3xl font-bold mb-3" style={{color: 'var(--primary)'}}>{program.title}</h1>
      <p className="text-slate-700 mb-6">{program.desc}</p>

      <div className="rounded-lg p-6 bg-gradient-to-br from-blue-50 to-white" style={{boxShadow: '0 2px 8px rgba(10,61,98,0.06)'}}>
        <p className="text-slate-800 leading-relaxed">{program.long}</p>
      </div>
    </div>
  )
}
